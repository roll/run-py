import unittest
from unittest.mock import Mock
from run.task.dependency import TaskDependency

class TaskDependencyTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockDependency = self._make_mock_dependency_class()
        self.tasks = ['task1', 'task2']
        self.args = ('arg',)
        self.kwargs = {'kwarg': 'kwarg'}
        self.dependency = MockDependency(
            self.tasks, *self.args, **self.kwargs)
        self.attribute = Mock(meta_module=Mock(
            task1=Mock(), task2=Mock()))        
        
    def test___call__(self):
        function = 'function'
        decorated = self.dependency(function)
        self.assertIsInstance(decorated, self.dependency._builder_class)
        self.dependency._method_task_class.assert_called_with(function)
        self.dependency._add_dependency.assert_called_with(decorated)
        
    def test___call__with_method_is_builder(self):
        builder = self.dependency._method_task_class('method')
        decorated = self.dependency(builder)
        self.assertIs(decorated, builder)
        self.dependency._add_dependency.assert_called_with(decorated)
        
    def test_resolve(self):
        self.dependency.resolve(self.attribute)
        (self.attribute.meta_module.task1.
            assert_called_with('arg', kwarg='kwarg'))
        (self.attribute.meta_module.task2.
            assert_called_with('arg', kwarg='kwarg'))        
        
    #Protected
    
    def _make_mock_dependency_class(self):
        class MockDependency(TaskDependency):
            #Public
            is_resolved = False
            #Protected
            _builder_class = Mock
            _method_task_class = Mock(return_value=Mock(
                require=Mock(), 
                trigger=Mock()))
            _add_dependency = Mock()
        return MockDependency          