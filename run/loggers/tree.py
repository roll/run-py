import logging
from ..helpers import sformat, pack
from ..task import CallTaskEvent
from ..settings import settings


class TreeLogger:

    # Public

    def __init__(self):
        self.__stack = []

    def __call__(self, event):
        logger = logging.getLogger('task')
        if isinstance(event, CallTaskEvent):
            if event.state == event.INIT:
                message = ''
                message += (len(self.__stack) - 1) * '│  '
                if self.__stack:
                    message += '├──'
                message += event.task.meta_qualname
                message += pack(*event.args, **event.kwargs)
                logger.info(message)
                self.__stack.append(event)
            elif event.state == event.DONE:
                self.__stack.pop()
                message = ''
                message += len(self.__stack) * '│  '
                message += '└──'
                message += '[10 ms]'
                message = sformat(message, 'done', settings.styles)
                logger.info(message)
            elif event.state == event.FAIL:
                self.__stack.pop()
                message = ''
                message += len(self.__stack) * '│  '
                message += '└──'
                message += '[fail]'
                message = sformat(message, 'fail', settings.styles)
                logger.info(message)

    def __repr__(self):
        return '<TreeLogger>'
