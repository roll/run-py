import unittest
from unittest.mock import Mock
from run.task.decorator import TaskDecorator, require, trigger

#TODO: refactor

#Tests

class TaskDecoratorTest(unittest.TestCase):

    #Public
    
    def test_with_method_is_builder(self):
        tasks = ['task1', 'task2']
        decorators = [MockRequire(tasks), MockTrigger(tasks)]
        for decorator in decorators:
            builder = MockBuilder('method')
            builder = decorator(builder)
            getattr(builder, decorator.name).assert_called_with(tasks)
        
    def test_with_raw_method(self):
        tasks = ['task1', 'task2']
        decorators = [MockRequire(tasks), MockTrigger(tasks)]
        for decorator in decorators:
            builder = decorator('method')
            self.assertEqual(builder.method, 'method')
            getattr(builder, decorator.name).assert_called_with(tasks)
            

#Fixtures

class MockBuilder:

    #Public

    require = Mock()
    trigger = Mock()
    
    def __init__(self, method):
        self.method = method
 

class MockAttribute:

    #Public

    def __new__(cls, method, *args, **kwargs):
        return MockBuilder(method) 
    
    
class MockTaskDecorator(TaskDecorator):

    #Public

    _builder_class = MockBuilder
    _attribute_class = MockAttribute
    

class MockRequire(require, MockTaskDecorator): 
    
    #Public
    
    name = 'require'
    
        
class MockTrigger(trigger, MockTaskDecorator):    
    
    #Public
    
    name = 'trigger'