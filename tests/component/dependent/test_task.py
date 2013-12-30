import unittest
from run.dependent.task import DependentAttributeTask

#Tests

class DependentAttributeTaskTest(unittest.TestCase):

    #Public

    def test(self):
        attr = MockAttribute()
        task = DependentAttributeTask('task')
        self.assertEqual(task.name, 'task')
        self.assertEqual(task.args, ())
        self.assertEqual(task.kwargs, {})
        self.assertEqual(task.is_executed, False)
        self.assertEqual(task(attr), ((), {}))
        self.assertEqual(task.is_executed, True)
    
    def test_with_args(self):
        attr = MockAttribute()
        task = DependentAttributeTask(('task', ('arg',)))
        self.assertEqual(task.name, 'task')
        self.assertEqual(task.args, ('arg',))
        self.assertEqual(task.kwargs, {})
        self.assertEqual(task.is_executed, False)
        self.assertEqual(task(attr), (('arg',),{}))
        self.assertEqual(task.is_executed, True)
        
    def test_with_args_and_kwargs(self):
        attr = MockAttribute()
        task = DependentAttributeTask(('task', ('arg',), {'kwarg': 'kwarg'}))
        self.assertEqual(task.name, 'task')
        self.assertEqual(task.args, ('arg',))
        self.assertEqual(task.kwargs, {'kwarg': 'kwarg'})
        self.assertEqual(task.is_executed, False)
        self.assertEqual(task(attr), (('arg',), {'kwarg': 'kwarg'}))
        self.assertEqual(task.is_executed, True)        
    
    
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