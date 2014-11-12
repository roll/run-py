import logging
from ..helpers import pack
from ..task import CallTaskEvent
from ..utils import stylize


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
                message = stylize(message, style='init')
                logger.info(message)
                self.__stack.append(event)
            elif event.state == event.DONE:
                init = self.__stack.pop()
                time = (event.time - init.time) * 1000
                message = ''
                message += len(self.__stack) * '│  '
                message += '└──'
                message += '[{time:.2f} ms] '.format(time=time)
                message = stylize(message, style='done')
                logger.info(message)
            elif event.state == event.FAIL:
                self.__stack.pop()
                message = ''
                message += len(self.__stack) * '│  '
                message += '└──'
                message += '[fail]'
                message = stylize(message, style='fail')
                logger.info(message)

    def __repr__(self):
        return '<TreeLogger>'
