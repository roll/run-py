import unittest
from unittest.mock import Mock, call
from run.var.var import Var

class VarTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockVar = self._make_mock_var_class()
        self.var = MockVar(meta_module=None)

    def test___get__(self):
        self.assertEqual(self.var.__get__('module'), 'value')
        self.var.invoke.assert_called_with()
        self.var._meta_initiated_signal_class.assert_called_with(self.var)
        self.var._meta_successed_signal_class.assert_called_with(self.var)
        self.var.meta_dispatcher.add_signal.assert_has_calls(
            [call('initiated_signal'), call('successed_signal')])
        
    def test___set__(self):
        self.var.__set__('module', 'new_value')
        self.assertEqual(self.var.__get__('module'), 'new_value')
        
    #Protected
    
    def _make_mock_var_class(self):
        class MockVar(Var):
            #Public
            invoke = Mock(return_value='value')
            meta_dispatcher = Mock(add_signal = Mock())
            #Protected
            _meta_initiated_signal_class = Mock(return_value='initiated_signal')
            _meta_successed_signal_class = Mock(return_value='successed_signal')
        return MockVar