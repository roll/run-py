import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.signal.dispatcher')


class DispatcherTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.handler = Mock()
        self.dispatcher = component.Dispatcher()

    # Tests

    def test___repr__(self):
        self.assertTrue(repr(self.dispatcher))

    def test_add_handler_and_add_signal(self):
        self.dispatcher.add_handler(self.handler)
        self.dispatcher.add_signal('signal')
        self.handler.handle.assert_called_with('signal')
