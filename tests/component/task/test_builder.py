import unittest
from unittest.mock import Mock
from run.task.builder import TaskBuilder

class TaskBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockBuilder = self._make_mock_builder_class()
        self.builder = MockBuilder(None)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}

    def test_require(self):
        self.builder.require(*self.args, **self.kwargs)
        self.builder._call_class.assert_called_with(
            'require', *self.args, **self.kwargs)
        
    def test_trigger(self):
        self.builder.trigger(*self.args, **self.kwargs)
        self.builder._call_class.assert_called_with(
            'trigger', *self.args, **self.kwargs)
        
    #Protected
    
    def _make_mock_builder_class(self):
        class MockBuilder(TaskBuilder):
            #Protected
            _call_class = Mock()
        return MockBuilder  