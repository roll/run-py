import logging
from ..signal import CallbackHandler
from ..task import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal


class Controller:

    # Public

    def __init__(self, dispatcher, stack=None):
        self._dispatcher = dispatcher
        self._stack = stack

    def listen(self):
        self._dispatcher.add_handler(
            self._CallbackHandler(
                self._on_initiated_task,
                signals=[self._InitiatedTaskSignal]))
        self._dispatcher.add_handler(
            self._CallbackHandler(
                self._on_successed_task,
                signals=[self._SuccessedTaskSignal]))
        self._dispatcher.add_handler(
            self._CallbackHandler(
                self._on_failed_task,
                signals=[self._FailedTaskSignal]))

    # Protected

    _CallbackHandler = CallbackHandler
    _FailedTaskSignal = FailedTaskSignal
    _InitiatedTaskSignal = InitiatedTaskSignal
    _SuccessedTaskSignal = SuccessedTaskSignal

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
