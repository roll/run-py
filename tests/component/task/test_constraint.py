import unittest
from unittest.mock import Mock
from run.task.constraint import TaskConstraint, require, trigger

class TaskConstraintTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockConstraint = self._make_mock_constraint_class()
        self.tasks = ['task1', 'task2']
        self.constraint = MockConstraint(self.tasks)
    
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


class require_Test(TaskConstraintTest):

    #Public

    def test__apply_dependency(self):
        tasks = ['task1', 'task2']
        builder = self.constraint._attribute_class()
        constraint = require(tasks)
        constraint._apply_dependency(builder)
        builder.require.assert_called_with(tasks)
        
        
class trigger_Test(TaskConstraintTest):

    #Public

    def test__apply_dependency(self):
        tasks = ['task1', 'task2']
        builder = self.constraint._attribute_class()
        constraint = trigger(tasks)
        constraint._apply_dependency(builder)
        builder.trigger.assert_called_with(tasks)