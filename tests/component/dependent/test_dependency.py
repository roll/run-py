import unittest
from unittest.mock import Mock
from run.dependent.dependency import DependentAttributeDependency

class DependentAttributeTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.dependency = DependentAttributeDependency('task')
        self.attribute = Mock(meta_module=Mock(task=Mock()))
        
    def test_resolve(self):
        self.dependency.resolve(self.attribute)
        self.attribute.meta_module.task.assert_called_with()

    def test_name(self):
        self.assertEqual(self.dependency.name, 'task')
        
    def test_args(self):
        self.assertEqual(self.dependency.args, ())
        
    def test_kwargs(self):
        self.assertEqual(self.dependency.kwargs, {})
        
    def test_is_resolved(self):
        self.assertEqual(self.dependency.is_resolved, False)
        
        
class DependentAttributeTaskTest_with_args_and_kwargs(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg',)
        self.kwargs = {'kwarg': 'kwarg'}
        self.dependency = DependentAttributeDependency(
            ('task', self.args, self.kwargs))
        self.attribute = Mock(meta_module=Mock(task=Mock()))
        
    def test_resolve(self):
        self.dependency.resolve(self.attribute)
        self.attribute.meta_module.task.assert_called_with(
            *self.args, **self.kwargs)
        
    def test_args(self):
        self.assertEqual(self.dependency.args, ('arg',))
        
    def test_kwargs(self):
        self.assertEqual(self.dependency.kwargs, {'kwarg': 'kwarg'})       