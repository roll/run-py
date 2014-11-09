import logging
from ..helpers import sformat
from ..task import CallTaskSignal, DoneTaskSignal, FailTaskSignal
from ..settings import settings  # @UnusedImport


class Controller:

    # Public

    def __init__(self, *, compact=settings.compact, plain=settings.plain):
        self.__compact = compact
        self.__plain = plain
        self.__stack = []

    def __call__(self, signal):
        logger = logging.getLogger('task')
        if isinstance(signal, CallTaskSignal):
            message = ''
            message += (len(self.__stack) - 1) * '│  '
            if self.__stack:
                message += '├──'
            message += signal.task.meta_qualname or 'main'
            logger.info(message)
            self.__stack.append(signal.task)
        elif isinstance(signal, DoneTaskSignal):
            self.__stack.pop()
            message = ''
            message += len(self.__stack) * '│  '
            message += '└──'
            message += '[10 ms]'
            message = sformat(message, 'successed', settings.styles)
            logger.info(message)
        elif isinstance(signal, FailTaskSignal):
            self.__stack.pop()
            message = ''
            message += len(self.__stack) * '│  '
            message += '└──'
            message += '[fail]'
            message = sformat(message, 'failed', settings.styles)
            logger.info(message)
