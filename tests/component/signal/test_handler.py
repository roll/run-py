import unittest
from unittest.mock import Mock
from run.signal.handler import CallbackHandler


class CallbackHandlerTest(unittest.TestCase):

    # Public

    def test_handle(self):
        callback = Mock()
        signal = Mock()
        handler = CallbackHandler(callback, signals=[Mock])
        handler.handle(signal)
        callback.assert_called_with(signal)
