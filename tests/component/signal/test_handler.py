import unittest
from unittest.mock import Mock
from run.signal.handler import CallbackHandler


class CallbackHandlerTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.callback = Mock()
        self.signal = Mock()

    def test_handle(self):
        self.handler = CallbackHandler(self.callback)
        self.handler.handle(self.signal)
        # Check callback call
        self.assertFalse(self.callback.called)

    def test_handle_with_signals(self):
        self.handler = CallbackHandler(self.callback, signals=[Mock])
        self.handler.handle(self.signal)
        # Check callback call
        self.callback.assert_called_with(self.signal)
