import unittest
from unittest.mock import Mock
from run.dependent.task import DependentAttributeTask

class DependentAttributeTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.task = DependentAttributeTask('task')
        self.attribute = Mock(meta_module=Mock(task=Mock()))
        
    def test___call__(self):
        self.task(self.attribute)
        self.attribute.meta_module.task.assert_called_with()

    def test_name(self):
        self.assertEqual(self.task.name, 'task')
        
    def test_args(self):
        self.assertEqual(self.task.args, ())
        
    def test_kwargs(self):
        self.assertEqual(self.task.kwargs, {})
        
    def test_is_processed(self):
        self.assertEqual(self.task.is_processed, False)
        
        
class DependentAttributeTaskTest_with_args_and_kwargs(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg',)
        self.kwargs = {'kwarg': 'kwarg'}
        self.task = DependentAttributeTask(('task', self.args, self.kwargs))
        self.attribute = Mock(meta_module=Mock(task=Mock()))
        
    def test___call__(self):
        self.task(self.attribute)
        self.attribute.meta_module.task.assert_called_with(
            *self.args, **self.kwargs)
        
    def test_args(self):
        self.assertEqual(self.task.args, ('arg',))
        
    def test_kwargs(self):
        self.assertEqual(self.task.kwargs, {'kwarg': 'kwarg'})       