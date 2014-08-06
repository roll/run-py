import unittest
from functools import partial
from unittest.mock import Mock, call, patch
from run.machine.controller import Controller

class ControllerTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Controller = self._make_mock_controller_class()
        self.dispatcher = Mock(add_handler=Mock())
        self.stack = Mock(__repr__=Mock(
            return_value='stack'), push=Mock(), pop=Mock())
        self.pcontroller = partial(
            self.Controller, self.dispatcher, stack=self.stack)
        self.signal = Mock(task=Mock(meta_qualname='attr_qualname'))

    def test_listen(self):
        controller = self.pcontroller()
        controller.listen()
        controller._CallbackHandler.assert_has_calls([
            call(controller._on_initiated_task, signals=['initiated_task']),
            call(controller._on_successed_task, signals=['successed_task']),
            call(controller._on_failed_task, signals=['failed_task'])])
        self.dispatcher.add_handler.assert_has_calls([
            call(controller._CallbackHandler.return_value),
            call(controller._CallbackHandler.return_value),
            call(controller._CallbackHandler.return_value)])

    def test__on_initiated_task(self):
        controller = self.pcontroller()
        controller._on_initiated_task(self.signal)
        self.stack.push.assert_called_with(self.signal.task)

    @patch('run.machine.controller.logging')
    def test__on_successed_task(self, logging):
        controller = self.pcontroller()
        controller._on_successed_task(self.signal)
        # Stack calls
        self.stack.__repr__.assert_called_with()
        self.stack.pop.assert_called_with()
        # Logging calls
        logging.getLogger.assert_called_with('successed')
        logging.getLogger.return_value.info.assert_called_with('stack')

    @patch('run.machine.controller.logging')
    def test__on_successed_task_with_stack_is_none(self, logging):
        controller = self.pcontroller(stack=None)
        controller._on_successed_task(self.signal)
        # Logging calls
        logging.getLogger.assert_called_with('successed')
        logging.getLogger.return_value.info.assert_called_with('attr_qualname')

    @patch('run.machine.controller.logging')
    def test__on_failed_task(self, logging):
        controller = self.pcontroller()
        controller._on_failed_task(self.signal)
        # Stack calls
        self.stack.__repr__.assert_called_with()
        self.stack.pop.assert_called_with()
        # Logging calls
        logging.getLogger.assert_called_with('failed')
        logging.getLogger.return_value.info.assert_called_with('stack')

    @patch('run.machine.controller.logging')
    def test__on_failed_task_with_stack_is_none(self, logging):
        controller = self.pcontroller(stack=None)
        controller._on_failed_task(self.signal)
        # Logging calls
        logging.getLogger.assert_called_with('failed')
        logging.getLogger.return_value.info.assert_called_with('attr_qualname')

    # Protected

    def _make_mock_controller_class(self):
        class MockController(Controller):
            # Protected
            _CallbackHandler = Mock(return_value=Mock())
            _FailedTaskSignal = 'failed_task'
            _InitiatedTaskSignal = 'initiated_task'
            _SuccessedTaskSignal = 'successed_task'
        return MockController
