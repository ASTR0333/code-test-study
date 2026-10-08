"""Compute the article's tables from real replay logs, without calling a model."""
import argparse,csv,json,collections,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def stage_pass(r,budget=None):
    if not r.get('base_pass'):return False
    if budget==0:return True
    if r['status']=='pass':return True
    if r['status']=='mismatch':rank=r['plus_first_failure_rank']
    elif r['status']=='timeout' and r.get('phase')=='plus':rank=r['current_rank']
    else:raise ValueError('Unresolved evaluation error: '+str(r))
    return budget is not None and rank>min(budget,r['plus_n'])

def analyze(folder='results/final',out='results/analysis',control_folder='results/control'):
    rows=json.loads((ROOT/folder/'results.json').read_text(encoding='utf8'))
    control=json.loads((ROOT/control_folder/'results.json').read_text(encoding='utf8'))
    excluded={r['task_id'] for r in control if r['status']!='pass'}
    assert excluded=={'HumanEval/32'},excluded
    assert len(rows)==328 and len({(r['model'],r['task_id']) for r in rows})==328
    assert not any(r['status'] in ['worker_error','task_timeout','oracle_error'] for r in rows)
    summary={'excluded':sorted(excluded),'exclusion_reason':'Canonical find_zero fails the residual oracle at atol=0.0001 on HumanEval/32; exclusion applied equally to both corpora. All raw outcomes remain available.','models':{},'source_results':folder,'control':control_folder,'n_tasks':163}
    for model in dict.fromkeys(r['model'] for r in rows):
        r=[x for x in rows if x['model']==model and x['task_id'] not in excluded]
        counts=[sum(stage_pass(x,b) for x in r) for b in [0,10,100,None]]
        extra=[x for x in r if x.get('base_pass') and x['status']!='pass']
        summary['models'][model]={'n':len(r),'base':counts[0],'plus10':counts[1],'plus100':counts[2],'full':counts[3],'base_percent':100*counts[0]/len(r),'full_percent':100*counts[3]/len(r),'drop_pp':100*(counts[0]-counts[3])/len(r),'additional_rejections':len(extra),'additional_wrong_values':sum(x['status']=='mismatch' for x in extra),'additional_timeouts':sum(x['status']=='timeout' for x in extra),'conditional_rejection_percent':100*len(extra)/counts[0],'status_counts':dict(collections.Counter(x['status'] for x in r)),'additional_cases':extra}
    dest=ROOT/out;dest.mkdir(parents=True,exist_ok=True)
    (dest/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
    with (dest/'task_results.csv').open('w',encoding='utf-8-sig',newline='') as f:
        fields=['model','task_id','included','status','base','plus10','plus100','full','failure_rank']
        writer=csv.DictWriter(f,fields);writer.writeheader()
        for r in rows:
            included=r['task_id'] not in excluded
            d={'model':r['model'],'task_id':r['task_id'],'included':included,'status':r['status'],'failure_rank':r.get('plus_first_failure_rank') or (r.get('current_rank') if r['status']=='timeout' else '')}
            for name,budget in [('base',0),('plus10',10),('plus100',100),('full',None)]:d[name]=int(stage_pass(r,budget)) if included else ''
            writer.writerow(d)
    lines=['# Результаты повторной проверки','',f"Задач в основном анализе: {summary['n_tasks']}. Исключена HumanEval/32 по результату контроля эталонной программы.",'','| Корпус | Базовые | +10 | +100 | Все | Дополнительные отказы |','|---|---:|---:|---:|---:|---:|']
    for m,s in summary['models'].items():lines.append(f"| {m} | {s['base']} | {s['plus10']} | {s['plus100']} | {s['full']} | {s['additional_rejections']} |")
    (dest/'summary.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    print(json.dumps({m:{k:v for k,v in s.items() if k!='additional_cases'} for m,s in summary['models'].items()},ensure_ascii=False,indent=2))
    return summary

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--results',default='results/final');p.add_argument('--out',default='results/analysis');p.add_argument('--control',default='results/control');a=p.parse_args();analyze(a.results,a.out,a.control)
