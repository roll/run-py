import logging
from ..signal import CallbackHandler
# TODO: remove task dependency, may be using settings IoC?
from ..task import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal

class Controller:

    # Public

    def __init__(self, dispatcher, stack=None):
        self._dispatcher = dispatcher
        self._stack = stack

    def listen(self):
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_initiated_task,
                signals=[self._initiated_task_signal_class]))
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_successed_task,
                signals=[self._successed_task_signal_class]))
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_failed_task,
                signals=[self._failed_task_signal_class]))

    # Protected

    _callback_handler_class = CallbackHandler
    _failed_task_signal_class = FailedTaskSignal
    _initiated_task_signal_class = InitiatedTaskSignal
    _successed_task_signal_class = SuccessedTaskSignal

    def _on_initiated_task(self, signal):
        if self._stack is not None:
            self._stack.push(signal.task)

    def _on_successed_task(self, signal):
        if self._stack is not None:
            message = repr(self._stack)
            self._stack.pop()
        else:
            message = signal.task.meta_qualname
        logger = logging.getLogger('successed')
        logger.info(message)

    def _on_failed_task(self, signal):
        if self._stack is not None:
            message = repr(self._stack)
            self._stack.pop()
        else:
            message = signal.task.meta_qualname
        logger = logging.getLogger('failed')
        logger.info(message)
