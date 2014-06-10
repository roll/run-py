import unittest
from io import StringIO
from unittest.mock import patch
from run import Module, Task, Var

#Tests

class ModuleTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.stdout = self.patcher.start()
        self.addCleanup(patch.stopall)        
        self.module = MockModule(meta_module=None)
        
    def test_list(self):
        self.module.list()
        self.assertEqual(
            self.stdout.getvalue(), 
            'default\n'
            'info\n'
            'list\n'
            'meta\n'
            'method_task\n'
            'module\n'
            'property_var\n'
            'task\n'
            'value_var\n'
            'var\n')
        
        
#Fixtures

class MockSubmodule(Module):
    
    #Vars
    
    module_var = True
    

class MockTask(Task):
    
    #Public
    
    def invoke(self, *args, **kwargs):
        pass
    
    
class MockVar(Var):
    
    #Public
    
    def invoke(self, *args, **kwargs):
        pass    


class MockModule(Module):

    #Classes
    
    class class_var:
        pass
    
    #Modules
    
    module = MockSubmodule()

    #Tasks
    
    task = MockTask()
    
    def method_task(self):
        pass    
    
    #Vars
    
    var = MockVar()
    value_var = True
    
    @property
    def property_var(self):
        pass