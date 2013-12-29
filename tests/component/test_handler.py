import unittest
from unittest.mock import Mock
from run.handler import CallbackHandler

#Tests

class CallbackHandlerTest(unittest.TestCase):

    #Public

    def test(self):
        callback = Mock()
        signal = MockSignal()
        handler = CallbackHandler(callback, signals=[MockSignal])
        handler.handle(signal)
        callback.assert_called_with(signal)
        
    
#Fixtures

class MockSignal: pass    