import unittest
from unittest.mock import Mock
from run.dependent.task import DependentAttributeTask

#Tests

class DependentAttributeTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.task = DependentAttributeTask('task')
        
    def test___call__(self):
        attr = MockAttribute()
        attr.meta_module.task.reset_mock()
        self.task(attr)
        attr.meta_module.task.assert_called_with()

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
        self.args = ('arg',)
        self.kwargs = {'kwarg': 'kwarg'}
        self.task = DependentAttributeTask(('task', self.args, self.kwargs))
        
    def test___call__(self):
        attr = MockAttribute()
        attr.meta_module.task.reset_mock()
        self.task(attr)
        attr.meta_module.task.assert_called_with(*self.args, **self.kwargs)
        
    def test_args(self):
        self.assertEqual(self.task.args, ('arg',))
        
    def test_kwargs(self):
        self.assertEqual(self.task.kwargs, {'kwarg': 'kwarg'})       
    
    
#Fixtures

class MockAttribute:
    
    #Public
    
    meta_module = Mock(task=Mock())