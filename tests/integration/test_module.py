import unittest
from run import Module, Task, Var

#Tests

class ModuleTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.run = MockMainModule(meta_module=None)
        
    def test_list(self):
        self.run.list()
        
        
#Fixtures

class MockModule(Module):
    
    #Protected
    
    module_var = True
    

class MockTask(Task):
    
    #Protected
    
    def invoke(self, *args, **kwargs):
        pass
    
    
class MockVar(Var):
    
    #Protected
    
    def invoke(self, *args, **kwargs):
        pass    


class MockMainModule(Module):

    #Public
    
    module = MockModule()

    task = MockTask()
    var = MockVar()
    
    value_var = True
    
    def method_task(self):
        pass
    
    @property
    def property_var(self):
        pass
    
    class class_var:
        pass