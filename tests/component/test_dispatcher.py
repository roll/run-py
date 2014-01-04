import unittest
from unittest.mock import Mock
from run.dispatcher import Dispatcher

class DispatcherTest(unittest.TestCase):

    #Public

    def test_add_handler_and_add_signal(self):
        handler = Mock(handle=Mock() )
        dispatcher = Dispatcher()
        dispatcher.add_handler(handler)
        dispatcher.add_signal('signal')
        handler.handle.assert_called_with('signal')     