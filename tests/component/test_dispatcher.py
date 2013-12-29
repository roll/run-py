import unittest
from unittest.mock import Mock
from run.dispatcher import Dispatcher

#Tests

class DispatcherTest(unittest.TestCase):

    #Public

    def test(self):
        handler = MockHandler()
        dispatcher = Dispatcher()
        dispatcher.add_handler(handler)
        dispatcher.add_signal('signal')
        handler.handle.assert_called_with('signal')
     
 
#Fixtures

class MockHandler:
    
    #Public
    
    handle = Mock()       