import unittest
from run import Run, Task, Var

#Tests

class RunTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.run = MockRun()
        
    def test_help(self):
        print(self.run.help())
        
        
#Fixtures

class MockTask(Task):
    
    def complete(self, *args, **kwargs):
        pass
    
    
class MockVar(Var):
    
    def retrieve(self, *args, **kwargs):
        pass    


class MockRun(Run):
    
    task = MockTask()
    var = MockVar()