import unittest
from unittest.mock import Mock
from run.signal.dispatcher import Dispatcher

class DispatcherTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.handler = Mock()
        self.dispatcher = Dispatcher()

    def test___repr__(self):
        self.assertTrue(repr(self.dispatcher))

    def test_add_handler_and_add_signal(self):
        self.dispatcher.add_handler(self.handler)
        self.dispatcher.add_signal('signal')
        self.handler.handle.assert_called_with('signal')
