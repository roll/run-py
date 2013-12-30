import unittest
from unittest.mock import Mock
from run.var.var import Var

#Tests

class VarTest(unittest.TestCase):

    #Public

    def test(self):
        pass
    

#Fixtures

class MockDispatcher:

    #Public

    add_signal = Mock()
    

class MockVar(Var):

    #Protected

    _dispatcher = MockDispatcher()
    _initiated_signal_class = Mock(return_value='signal')
    _retrieved_signal_class = Mock(return_value='signal')