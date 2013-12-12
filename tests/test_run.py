import os
import unittest
from run import Run, Task, ParsedVar

#Tests

class RunTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.run = MockRun()
        
    def test_list(self):
        print(self.run.list())
        
        
#Fixtures

class MockTask(Task):
    
    def complete(self, *args, **kwargs):
        pass
    

class MockRun(Run):
    
    task = MockTask()
    var = ParsedVar('test_run.py', 'import (.*test)\n', 
                    base_dir=os.path.dirname(__file__))