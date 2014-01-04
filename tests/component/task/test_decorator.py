import unittest
from unittest.mock import Mock
from run.task.decorator import TaskDecorator, require, trigger

class TaskDecoratorTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockTaskDecorator = self._make_mock_task_decorator_class()
        self.tasks = ['task1', 'task2']
        self.decorator = MockTaskDecorator(self.tasks)
    
    def test___call__with_function_is_builder(self):
        builder = self.decorator._attribute_class('method')
        decorated = self.decorator(builder)
        self.assertIs(decorated, builder)
        self.decorator._add_dependency.assert_called_with(decorated)
        
    def test___call__with_function_is_raw_function(self):
        function = 'function'
        decorated = self.decorator(function)
        self.assertIsInstance(decorated, self.decorator._builder_class)
        self.decorator._attribute_class.assert_called_with(function)
        self.decorator._add_dependency.assert_called_with(decorated)
        
    #Protected
    
    def _make_mock_task_decorator_class(self):
        class MockTaskDecorator(TaskDecorator):
            #Protected
            _builder_class = Mock
            _attribute_class = Mock(return_value=Mock(
                require=Mock(), 
                trigger=Mock()))
            _add_dependency = Mock()
        return MockTaskDecorator


class requireTest(TaskDecoratorTest):

    #Public

    def test__add_dependency(self):
        tasks = ['task1', 'task2']
        builder = self.decorator._attribute_class()
        decorator = require(tasks)
        decorator._add_dependency(builder)
        builder.require.assert_called_with(tasks)
        
        
class triggerTest(TaskDecoratorTest):

    #Public

    def test__add_dependency(self):
        tasks = ['task1', 'task2']
        builder = self.decorator._attribute_class()
        decorator = trigger(tasks)
        decorator._add_dependency(builder)
        builder.trigger.assert_called_with(tasks)