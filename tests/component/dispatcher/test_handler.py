import unittest
from unittest.mock import Mock
from run.dispatcher.handler import DispatcherCallbackHandler

class DispatcherCallbackHandlerTest(unittest.TestCase):

    #Public

    def test_handle(self):
        callback = Mock()
        signal = Mock()
        handler = DispatcherCallbackHandler(callback, signals=[Mock])
        handler.handle(signal)
        callback.assert_called_with(signal)