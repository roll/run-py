import unittest
from unittest.mock import Mock
from run.task.prototype import TaskPrototype

class TaskPrototypeTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.MockPrototype = self._make_mock_prototype_class()
        self.prototype = self.MockPrototype('class', None)

    def test_require(self):
        self.prototype.require(*self.args, **self.kwargs)
        self.prototype._call_class.assert_called_with(
            'require', *self.args, **self.kwargs)
        
    def test_trigger(self):
        self.prototype.trigger(*self.args, **self.kwargs)
        self.prototype._call_class.assert_called_with(
            'trigger', *self.args, **self.kwargs)
        
    #Protected
    
    def _make_mock_prototype_class(self):
        class MockPrototype(TaskPrototype):
            #Protected
            _call_class = Mock()
        return MockPrototype 