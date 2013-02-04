import os
import sys
import unittest
from lib31.patcher import Patcher
from run.console.script import script
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
        script()
            
    def test_run_method(self):
        sys.argv = ['run', 'method', '-cClassToRun']
        script()             

    def test_list(self):
        sys.argv = ['run']
        script()
        
    def test_list_methods(self):
        sys.argv = ['run', '-cClassToRun']
        script()            

    def test_help(self):
        sys.argv = ['run', '-h']
        self.assertRaises(SystemExit, script)
            
    def test_help_method(self):
        sys.argv = ['run', 'method', '-cClassToRun', '-h']
        script()             
    
    def test_help_function(self):
        sys.argv = ['run', 'function_normal', '-h']
        script() 