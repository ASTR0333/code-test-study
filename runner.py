"""Replay a frozen public code corpus. Standard library + NumPy; no model API.

Only use with the included, hash-verified corpus. The Python namespace guard is
defence in depth, NOT a security sandbox for arbitrary new generated programs.
"""
from __future__ import annotations
import argparse,ast,builtins,collections,concurrent.futures,copy,gzip,hashlib,json,math,os,platform,random,subprocess,sys,threading,time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
ALLOWED={'typing','math','re','collections','fractions','hashlib','functools','itertools','heapq','bisect','string','random'}
REAL_IMPORT=builtins.__import__
REAL_EVAL=builtins.eval

def guarded_import(name,globals=None,locals=None,fromlist=(),level=0):
    if level or name.split('.')[0] not in ALLOWED:raise RuntimeError('Blocked import: '+name)
    return REAL_IMPORT(name,globals,locals,fromlist,level)

def arithmetic_eval(expr,*args,**kwargs):
    tree=ast.parse(expr,mode='eval')
    allowed=(ast.Expression,ast.BinOp,ast.UnaryOp,ast.Constant,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.FloorDiv,ast.Mod,ast.Pow,ast.USub,ast.UAdd)
    if any(not isinstance(n,allowed) for n in ast.walk(tree)):raise RuntimeError('Non-arithmetic eval')
    return REAL_EVAL(compile(tree,'<arithmetic>','eval'),{'__builtins__':{}},{})

def namespace(code):
    tree=ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node,ast.Attribute) and node.attr.startswith('__'):raise RuntimeError('Dunder attribute')
        if isinstance(node,ast.Import) and any(a.name.split('.')[0] not in ALLOWED for a in node.names):raise RuntimeError('Import rejected')
        if isinstance(node,ast.ImportFrom) and (node.level or node.module.split('.')[0] not in ALLOWED):raise RuntimeError('Import rejected')
    safe=dict(vars(builtins))
    for k in ['open','input','exec','compile','breakpoint','exit','quit','help']:safe.pop(k,None)
    safe['__import__']=guarded_import;safe['eval']=arithmetic_eval
    ns={'__builtins__':safe,'__name__':'__generated__'}
    exec(compile(tree,'<corpus>','exec'),ns)
    return ns

def equivalent(out,exp,inp,entry,atol):
    # HumanEval branch of EvalPlus v0.3.1 (MIT-origin evaluator; see licenses).
    if entry=='find_zero':return abs(sum(c*math.pow(out,i) for i,c in enumerate(inp[0])))<=atol
    if out==exp:return True
    floats=isinstance(exp,float) or (isinstance(exp,(tuple,list)) and bool(exp) and all(isinstance(x,float) for x in exp))
    if not atol and floats:atol=1e-6
    if atol:
        if type(out)!=type(exp):return False
        if isinstance(exp,(tuple,list)) and len(out)!=len(exp):return False
        return bool(np.allclose(out,exp,rtol=1e-7,atol=atol))
    return False

def read_tasks():
    return {t['task_id']:t for t in (json.loads(l) for l in gzip.open(ROOT/'data'/'HumanEvalPlus-v0.1.10.jsonl.gz','rt',encoding='utf8'))}

def clipped(value):
    s=repr(value)
    return s if len(s)<=1200 else s[:1200]+'...'

def worker(args):
    random.seed(20261008+args.task)
    t=read_tasks()['HumanEval/'+str(args.task)]
    model=args.worker
    outpath=Path(args.result)
    report={'model':model,'task_id':t['task_id'],'entry_point':t['entry_point'],'base_n':len(t['base_input']),'plus_n':len(t['plus_input']),'status':'running','base_pass':False,'base_executed':0,'plus_executed':0,'plus_first_failure_rank':None,'phase':'setup'}
    def save():outpath.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    deadline=[time.monotonic()+60]
    def watchdog():
        while True:
            time.sleep(.01)
            if time.monotonic()>deadline[0]:
                report['status']='timeout';report['error']='Per-call deadline exceeded';save();os._exit(124)
    threading.Thread(target=watchdog,daemon=True).start()
    code=t['prompt']+t['canonical_solution'] if model=='canonical' else (ROOT/'data'/model/('HumanEval_'+str(args.task)+'.py')).read_text(encoding='utf8')
    try:fn=namespace(code)[t['entry_point']]
    except Exception as e:
        report.update(status='load_error',error=type(e).__name__+': '+str(e));save();return
    try:ref=namespace(t['prompt']+t['canonical_solution'])[t['entry_point']]
    except Exception as e:
        report.update(status='oracle_error',error=repr(e));save();return
    permutation=list(range(len(t['plus_input'])))
    random.Random(20261008+args.task).shuffle(permutation)
    begin=time.perf_counter()
    for phase,indices in [('base',range(len(t['base_input']))),('plus',permutation)]:
        report['phase']=phase
        for rank,index in enumerate(indices,1):
            report['current_rank']=rank;report['current_input_index']=index
            inp=t[phase+'_input'][index]
            deadline[0]=time.monotonic()+60
            try:
                start=time.perf_counter();expected=ref(*copy.deepcopy(inp));ref_time=time.perf_counter()-start
            except Exception as e:
                report.update(status='oracle_error',error=repr(e));save();return
            deadline[0]=time.monotonic()+max(args.min_time,4*ref_time)
            try:
                actual=fn(*copy.deepcopy(inp))
                deadline[0]=time.monotonic()+60
                correct=equivalent(actual,expected,inp,t['entry_point'],t['atol'])
                err=None
            except Exception as e:
                deadline[0]=time.monotonic()+60
                correct=False;actual=None;err=type(e).__name__+': '+str(e)
            report[phase+'_executed']+=1
            if not correct:
                report.update(status='mismatch',failure={'phase':phase,'rank':rank,'input_index':index,'input':clipped(inp),'expected':clipped(expected),'actual':clipped(actual),'exception':err})
                if phase=='plus':report['plus_first_failure_rank']=rank
                report['elapsed_seconds']=time.perf_counter()-begin;save();return
        if phase=='base':report['base_pass']=True
    report.update(status='pass',elapsed_seconds=time.perf_counter()-begin)
    save()

def verify_data():
    manifest=json.loads((ROOT/'data'/'manifest.json').read_text(encoding='utf8'))
    for name,wanted in manifest['files'].items():
        actual=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        if actual!=wanted:raise ValueError('Data changed: '+name)
    return manifest

def main(args):
    manifest=verify_data()
    resultdir=ROOT/args.output;resultdir.mkdir(parents=True,exist_ok=True)
    models=['canonical'] if args.canonical else list(manifest['models'])
    tasks=range(164) if args.task<0 else [args.task]
    specs=[(m,i) for m in models for i in tasks]
    def run(spec):
        model,i=spec;path=resultdir/(model+'__'+str(i)+'.json')
        cmd=[sys.executable,'-I',str(Path(__file__).resolve()),'--worker',model,'--task',str(i),'--result',str(path),'--min-time',str(args.min_time)]
        started=time.perf_counter()
        try:
            p=subprocess.run(cmd,capture_output=True,text=True,timeout=180,encoding='utf8',errors='replace',cwd=ROOT)
            if not path.exists():return {'model':model,'task_id':'HumanEval/'+str(i),'status':'worker_error','error':p.stderr[-1500:]}
            row=json.loads(path.read_text(encoding='utf8'))
            row['returncode']=p.returncode
            if p.stderr:row['stderr']=p.stderr[-1500:]
        except subprocess.TimeoutExpired:
            row={'model':model,'task_id':'HumanEval/'+str(i),'status':'task_timeout','base_pass':False}
        row['wall_seconds']=time.perf_counter()-started
        path.write_text(json.dumps(row,ensure_ascii=False,indent=2),encoding='utf8')
        return row
    rows=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for row in pool.map(run,specs):
            rows.append(row)
            print(f"{len(rows)}/{len(specs)} {row['model']} {row['task_id']} {row['status']}",flush=True)
    (resultdir/'results.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
    env={'python':sys.version,'platform':platform.platform(),'numpy':np.__version__,'seed':manifest['seed'],'min_time_seconds':args.min_time,'time_factor':4,'jobs':args.jobs,'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (resultdir/'environment.json').write_text(json.dumps(env,indent=2),encoding='utf8')
    print('Saved',resultdir/'results.json')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--worker');p.add_argument('--task',type=int,default=-1);p.add_argument('--result');p.add_argument('--output',default='results/replay');p.add_argument('--jobs',type=int,default=2);p.add_argument('--canonical',action='store_true');p.add_argument('--min-time',type=float,default=1.0)
    args=p.parse_args()
    worker(args) if args.worker else main(args)
