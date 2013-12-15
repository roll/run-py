import unittest
from run import Run, Task, Var

#Tests

class RunTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.run = MockRun()
        
    def test_help(self):
        self.run.help()
        
        
#Fixtures

class MockTask(Task):
    
    #Protected
    
    def _complete(self, *args, **kwargs):
        pass
    
    
class MockVar(Var):
    
    #Protected
    
    def _retrieve(self, *args, **kwargs):
        pass    


class MockRun(Run):

    #Public

    task = MockTask()
    var = MockVar()
    
    value_var = 1
    
    @property
    def property_var(self):
        pass
    
    class class_var:
        pass