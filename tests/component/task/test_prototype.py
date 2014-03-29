import unittest
from unittest.mock import Mock
from run.task.prototype import TaskPrototype

class TaskBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockBuilder = self._make_mock_builder_class()
        self.prototype = MockBuilder(None)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}

    def test_require(self):
        self.prototype.require(*self.args, **self.kwargs)
        self.prototype._call_class.assert_called_with(
            'require', *self.args, **self.kwargs)
        
    def test_trigger(self):
        self.prototype.trigger(*self.args, **self.kwargs)
        self.prototype._call_class.assert_called_with(
            'trigger', *self.args, **self.kwargs)
        
    #Protected
    
    def _make_mock_builder_class(self):
        class MockPrototype(TaskPrototype):
            #Protected
            _call_class = Mock()
        return MockPrototype 