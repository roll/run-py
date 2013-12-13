import os
import unittest
from run import Run, Task

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
    
    
class MockVar(Task):
    
    def retrieve(self, *args, **kwargs):
        pass    
    

class MockRun(Run):
    
    task = MockTask()
    var = MockVar()