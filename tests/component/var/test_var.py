import unittest
from unittest.mock import Mock, call
from run.var.var import Var

#Tests

class VarTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.var = MockVar(module=None)

    def test___get__(self):
        self.assertEqual(self.var.__get__('module'), 'value')
        self.var.retrieve.assert_called_with()
        self.var._initiated_signal_class.assert_called_with(self.var)
        self.var._retrieved_signal_class.assert_called_with(self.var)
        self.var._dispatcher.add_signal.assert_has_calls(
            [call('initiated_signal'), call('retrieved_signal')])
        
    def test___set__(self):
        self.var.__set__('module', 'new_value')
        self.assertEqual(self.var.__get__('module'), 'new_value')
    

#Fixtures 

class MockVar(Var):
    
    #Public
    
    retrieve = Mock(return_value='value')

    #Protected

    _dispatcher = Mock(add_signal = Mock())
    _initiated_signal_class = Mock(return_value='initiated_signal')
    _retrieved_signal_class = Mock(return_value='retrieved_signal')