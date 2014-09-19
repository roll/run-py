import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.signal.function')


class FunctionHandlerTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.callback = Mock()
        self.signal = Mock()

    # Tests

    def test_handle(self):
        self.handler = component.FunctionHandler(self.callback)
        self.handler.handle(self.signal)
        # Check callback call
        self.assertFalse(self.callback.called)

    def test_handle_with_signals(self):
        self.handler = component.FunctionHandler(self.callback, signals=[Mock])
        self.handler.handle(self.signal)
        # Check callback call
        self.callback.assert_called_with(self.signal)
