import unittest
from unittest.mock import Mock
from run.task.dependency import TaskDependencyDecorator

class TaskDependencyDecoratorTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.builder = Mock(depend=Mock())
        self.MockDecorator = self._make_mock_decorator_class(self.builder)
        self.decorator = self.MockDecorator()       
        
    def test___call__(self):
        function = 'function'
        decorated = self.decorator(function)
        self.assertIs(decorated, self.builder)
        self.decorator._method_task_class.assert_called_with(function)
        self.builder.depend.assert_called_with(self.decorator._dependency) 
        
    def test___call__with_method_is_builder(self):
        decorated = self.decorator(self.builder)
        self.assertIs(decorated, self.builder)
        self.builder.depend.assert_called_with(self.decorator._dependency)      
        
    #Protected
    
    def _make_mock_decorator_class(self, builder):
        class MockDecorator(TaskDependencyDecorator):
            #Protected
            _builder_class = Mock
            _method_task_class = Mock(return_value=builder)
            _dependency = Mock()
        return MockDecorator          