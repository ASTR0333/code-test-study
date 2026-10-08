import unittest
from runner import equivalent,namespace,arithmetic_eval,verify_data
from analyze import stage_pass

class EvaluatorTests(unittest.TestCase):
    def test_float_tolerance(self):
        self.assertTrue(equivalent(1.0000001,1.0,[],'x',0))
        self.assertFalse(equivalent(1.01,1.0,[],'x',0))
    def test_sequence_length(self):
        self.assertFalse(equivalent([1.0,1.0],[1.0],[],'x',1e-6))
    def test_valid_alternate_root(self):
        self.assertTrue(equivalent(1.0,-1.0,[[-1,0,1]],'find_zero',1e-4))
        self.assertFalse(equivalent(0.0,-1.0,[[-1,0,1]],'find_zero',1e-4))
    def test_exact_values(self):
        self.assertTrue(equivalent([1,2],[1,2],[],'x',0))
        self.assertFalse(equivalent([1,2],[2,1],[],'x',0))
    def test_corpus_hashes(self):verify_data()
    def test_arithmetic(self):
        self.assertEqual(arithmetic_eval('2+3*4**2'),50)
        with self.assertRaises(RuntimeError):arithmetic_eval('__import__("os")')
    def test_restricted_namespace(self):
        with self.assertRaises(RuntimeError):namespace('import os')
        self.assertEqual(namespace('def f(x):\n return x+1')['f'](2),3)
    def test_budget_boundary(self):
        r={'base_pass':True,'status':'mismatch','plus_first_failure_rank':11,'plus_n':200}
        self.assertTrue(stage_pass(r,10));self.assertFalse(stage_pass(r,100));self.assertFalse(stage_pass(r))
    def test_timeout_boundary(self):
        r={'base_pass':True,'status':'timeout','phase':'plus','current_rank':5,'plus_n':10}
        self.assertTrue(stage_pass(r,0));self.assertFalse(stage_pass(r,10))
    def test_unresolved_is_error(self):
        with self.assertRaises(ValueError):stage_pass({'base_pass':True,'status':'worker_error'})

if __name__=='__main__':unittest.main()
