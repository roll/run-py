import unittest
from unittest.mock import Mock
from run.task.decorator import require, trigger

#Tests

class requireTest(unittest.TestCase):

    #Public
    
    def test_with_method_is_builder(self):
        require = MockRequire(['task1', 'task2'])
        method = MockBuilder('method')
        builder = require(method)
        self.assertEqual(method, builder)
        builder.require.assert_called_with(['task1', 'task2'])
        
    def test_with_raw_method(self):
        require = MockRequire(['task1', 'task2'])
        builder = require('method')
        self.assertEqual(builder.method, 'method')
        builder.require.assert_called_with(['task1', 'task2'])

    
class triggerTest(unittest.TestCase):

    #Public
    
    def test_with_method_is_builder(self):
        trigger = MockTrigger(['task1', 'task2'])
        method = MockBuilder('method')
        builder = trigger(method)
        self.assertEqual(method, builder)
        builder.trigger.assert_called_with(['task1', 'task2'])
        
    def test_with_raw_method(self):
        trigger = MockTrigger(['task1', 'task2'])
        builder = trigger('method')
        self.assertEqual(builder.method, 'method')
        builder.trigger.assert_called_with(['task1', 'task2'])
            

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
    
    
class MockRequire(require):

    #Public

    _builder_class = MockBuilder
    _attribute_class = MockAttribute
    
    
class MockTrigger(trigger):

    #Public

    _builder_class = MockBuilder
    _attribute_class = MockAttribute    