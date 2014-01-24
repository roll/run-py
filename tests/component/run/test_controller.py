import unittest
from functools import partial
from unittest.mock import Mock, call
from run.run.controller import RunController

class RunControllerTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockController = self._make_mock_controller_class()
        self.dispatcher = Mock(add_handler=Mock())
        self.stack = Mock(__str__=Mock(return_value='stack'), push=Mock(), pop=Mock())
        self.partial_controller = partial(MockController, self.dispatcher, stack=self.stack)
        self.signal = Mock(attribute=Mock(meta_qualname='attr_qualname'))
            
    def test_listen(self):
        controller = self.partial_controller()
        controller.listen()
        controller._callback_handler_class.assert_has_calls([
            call(controller._on_initiated_attribute, 
                 signals=['initiated_task', 'initiated_var']),
            call(controller._on_executed_attribute, 
                 signals=['completed_task', 'retrieved_var'])])
        self.dispatcher.add_handler.assert_has_calls([
            call(controller._callback_handler_class.return_value),
            call(controller._callback_handler_class.return_value)])
        
    def test__on_initiated_attribute(self):
        controller = self.partial_controller()
        controller._on_initiated_attribute(self.signal)
        self.stack.push.assert_called_with(self.signal.attribute)
        
    def test__on_executed_attribute(self):
        controller = self.partial_controller()
        controller._on_executed_attribute(self.signal)
        self.stack.__str__.assert_called_with()   
        self.stack.pop.assert_called_with()
        (controller._logging_module.getLogger.return_value.info.
            assert_called_with('stack'))
        
    def test__on_executed_attribute_with_stack_is_none(self):
        controller = self.partial_controller(stack=None)
        controller._on_executed_attribute(self.signal)
        (controller._logging_module.getLogger.return_value.info.
            assert_called_with('attr_qualname'))
    
    #Protected
    
    def _make_mock_controller_class(self):
        class MockController(RunController):
            #Protected
            _callback_handler_class = Mock(return_value=Mock())
            _initiated_task_signal_class = 'initiated_task'
            _initiated_var_signal_class = 'initiated_var'
            _completed_task_signal_class = 'completed_task'
            _retrieved_var_signal_class = 'retrieved_var'
            _logging_module = Mock(getLogger=Mock(
                return_value=Mock(info=Mock())))       
        return MockController