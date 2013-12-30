import unittest
from unittest.mock import Mock
from run.task.decorator import TaskDecorator, require, trigger

#Tests

class TaskDecoratorTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.tasks = ['task1', 'task2']
        self.decorator = MockTaskDecorator(self.tasks)
    
    def test_with_method_is_builder(self):
        builder = MockBuilder('method')
        decorated = self.decorator(builder)
        self.assertIs(decorated, builder)
        self.decorator._add_dependency.assert_called_with(decorated)
        
    def test_with_method_raw_method(self):
        method = 'method'
        decorated = self.decorator(method)
        self.assertIsInstance(decorated, MockBuilder)
        decorated.__init__.assert_called_with(method)
        self.decorator._add_dependency.assert_called_with(decorated)


class requireTest(unittest.TestCase):

    #Public

    def test__add_dependency(self):
        tasks = ['task1', 'task2']
        builder = MockBuilder()
        decorator = require(tasks)
        decorator._add_dependency(builder)
        builder.require.assert_called_with(tasks)
        
        
class triggerTest(unittest.TestCase):

    #Public

    def test__add_dependency(self):
        tasks = ['task1', 'task2']
        builder = MockBuilder()
        decorator = trigger(tasks)
        decorator._add_dependency(builder)
        builder.trigger.assert_called_with(tasks)        
            

#Fixtures

class MockBuilder:

    #Public
    
    __init__ = Mock(return_value=None)
    require = Mock()
    trigger = Mock()
    
    
class MockTaskDecorator(TaskDecorator):

    
    #Protected
    
    _builder_class = MockBuilder
    _attribute_class = lambda self, method: MockBuilder(method)
    _add_dependency = Mock()