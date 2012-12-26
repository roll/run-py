import os
import sys
import unittest
from lib31.utils.patcher import Patcher
from run.scripts.run import run
from .fixtures import process

#Environ
sys, process


#Tests
class RunTest(unittest.TestCase):
    
    PATCH = {
        'process.cwd': os.path.dirname(__file__),
        'sys.argv': [], #TODO: It's a hack! Replace by normal repatching in methods
    }
    
    def setUp(self):
        self.patcher = Patcher(globals())
        self.patcher.patch(self.PATCH) 
        
    def tearDown(self):
        self.patcher.restore()
    
    def test_run(self):
        sys.argv = ['run', 'function_normal', '1', 'b=test words']
        run()
            
    def test_run_method(self):
        sys.argv = ['run', 'method', '-cClassToRun']
        run()             

    def test_list(self):
        sys.argv = ['run']
        run()
        
    def test_list_methods(self):
        sys.argv = ['run', '-cClassToRun']
        run()            

    def test_help(self):
        sys.argv = ['run', '-h']
        self.assertRaises(SystemExit, run)
            
    def test_help_method(self):
        sys.argv = ['run', 'method', '-cClassToRun', '-h']
        run()             
    
    def test_help_function(self):
        sys.argv = ['run', 'function_normal', '-h']
        run() 