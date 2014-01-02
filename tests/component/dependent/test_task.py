import unittest
from run.dependent.task import DependentAttributeTask

#Tests

class DependentAttributeTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.task = DependentAttributeTask('task')
        
    def test___call__(self):
        attr = MockAttribute()
        self.assertEqual(self.task(attr), ((), {}))
        self.assertEqual(self.task.is_executed, True)

    def test_name(self):
        self.assertEqual(self.task.name, 'task')
        
    def test_args(self):
        self.assertEqual(self.task.args, ())
        
    def test_kwargs(self):
        self.assertEqual(self.task.kwargs, {})
        
    def test_is_executed(self):
        self.assertEqual(self.task.is_executed, False)
        
        
class DependentAttributeTaskTest_with_args_and_kwargs(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.task = DependentAttributeTask(
            ('task', ('arg',), {'kwarg': 'kwarg'}))
        
    def test___call__(self):
        attr = MockAttribute()
        self.assertEqual(self.task(attr), (('arg',), {'kwarg': 'kwarg'}))
        self.assertEqual(self.task.is_executed, True)
        
    def test_args(self):
        self.assertEqual(self.task.args, ('arg',))
        
    def test_kwargs(self):
        self.assertEqual(self.task.kwargs, {'kwarg': 'kwarg'})       
    
    
#Fixtures

class MockModule:
    
    #Public
    
    def task(self, *args, **kwargs):
        return (args, kwargs) 
    
    
class MockAttribute:
    
    #Public
    
    def __init__(self):
        self._module = MockModule()
    
    @property
    def meta_module(self):
        return self._module    