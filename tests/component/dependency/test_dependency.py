import unittest
from unittest.mock import Mock
from run.dependency.dependency import Dependency

class DependencyTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockConstraint = self._make_mock_constraint_class()
        self.tasks = ['task1', 'task2']
        self.constraint = MockConstraint(self.tasks)
        
    def setUp(self):
        self.dependency = TaskDependency('task')
        self.attribute = Mock(meta_module=Mock(task=Mock()))
        
    def test___call__with_function_is_builder(self):
        builder = self.constraint._attribute_class('method')
        decorated = self.constraint(builder)
        self.assertIs(decorated, builder)
        self.constraint._apply_dependency.assert_called_with(decorated)
        
    def test___call__with_function_is_raw_function(self):
        function = 'function'
        decorated = self.constraint(function)
        self.assertIsInstance(decorated, self.constraint._builder_class)
        self.constraint._attribute_class.assert_called_with(function)
        self.constraint._apply_dependency.assert_called_with(decorated)
        
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
        
    #Protected
    
    def _make_mock_constraint_class(self):
        class MockConstraint(TaskConstraint):
            #Protected
            _builder_class = Mock
            _attribute_class = Mock(return_value=Mock(
                require=Mock(), 
                trigger=Mock()))
            _apply_dependency = Mock()
        return MockConstraint
        
        
class DependencyTest_with_args_and_kwargs(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg',)
        self.kwargs = {'kwarg': 'kwarg'}
        self.dependency = TaskDependency(
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