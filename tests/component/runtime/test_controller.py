import unittest
from functools import partial
from unittest.mock import Mock, call, patch
from run.runtime.controller import Controller

class ControllerTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockController = self._make_mock_controller_class()
        self.dispatcher = Mock(add_handler=Mock())
        self.stack = Mock(__repr__=Mock(
            return_value='stack'), push=Mock(), pop=Mock())
        self.pcontroller = partial(MockController, 
            self.dispatcher, stack=self.stack)
        self.signal = Mock(attribute=Mock(meta_qualname='attr_qualname'))
            
    def test_listen(self):
        controller = self.pcontroller()
        controller.listen()
        controller._callback_handler_class.assert_has_calls([
            call(controller._on_initiated_task, signals=['initiated_task']),
            call(controller._on_successed_task, signals=['successed_task'])])
        self.dispatcher.add_handler.assert_has_calls([
            call(controller._callback_handler_class.return_value),
            call(controller._callback_handler_class.return_value)])
        
    def test__on_initiated_task(self):
        controller = self.pcontroller()
        controller._on_initiated_task(self.signal)
        self.stack.push.assert_called_with(self.signal.attribute)
     
    @patch('run.runtime.controller.logging')
    def test__on_successed_task(self, logging):
        controller = self.pcontroller()
        controller._on_successed_task(self.signal)
        self.stack.__repr__.assert_called_with()   
        self.stack.pop.assert_called_with()
        logging.getLogger.return_value.info.assert_called_with('stack')
    
    @patch('run.runtime.controller.logging')    
    def test__on_successed_task_with_stack_is_none(self, logging):
        controller = self.pcontroller(stack=None)
        controller._on_successed_task(self.signal)
        logging.getLogger.return_value.info.assert_called_with('attr_qualname')
    
    #Protected
    
    def _make_mock_controller_class(self):
        class MockController(Controller):
            #Protected
            _callback_handler_class = Mock(return_value=Mock())
            _initiated_task_signal_class = 'initiated_task'
            _successed_task_signal_class = 'successed_task'
        return MockController