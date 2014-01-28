import unittest
from unittest.mock import Mock
from run.task.dependency import TaskDependency, require, trigger

class TaskDependencyTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockDependency = self._make_mock_dependency_class()
        self.tasks = ['task1', 'task2']
        self.dependency = MockDependency(self.tasks)
    
    def test___call__with_function_is_builder(self):
        builder = self.dependency._attribute_class('method')
        decorated = self.dependency(builder)
        self.assertIs(decorated, builder)
        self.dependency._add_dependency.assert_called_with(decorated)
        
    def test___call__with_function_is_raw_function(self):
        function = 'function'
        decorated = self.dependency(function)
        self.assertIsInstance(decorated, self.dependency._builder_class)
        self.dependency._attribute_class.assert_called_with(function)
        self.dependency._add_dependency.assert_called_with(decorated)
        
    #Protected
    
    def _make_mock_dependency_class(self):
        class MockDependency(TaskDependency):
            #Protected
            _builder_class = Mock
            _attribute_class = Mock(return_value=Mock(
                require=Mock(), 
                trigger=Mock()))
            _add_dependency = Mock()
        return MockDependency


class requireTest(TaskDependencyTest):

    #Public

    def test__add_dependency(self):
        tasks = ['task1', 'task2']
        builder = self.dependency._attribute_class()
        dependency = require(tasks)
        dependency._add_dependency(builder)
        builder.require.assert_called_with(tasks)
        
        
class triggerTest(TaskDependencyTest):

    #Public

    def test__add_dependency(self):
        tasks = ['task1', 'task2']
        builder = self.dependency._attribute_class()
        dependency = trigger(tasks)
        dependency._add_dependency(builder)
        builder.trigger.assert_called_with(tasks)