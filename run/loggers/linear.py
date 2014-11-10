import logging
from ..helpers import sformat, pack
from ..task import CallTaskEvent
from ..settings import settings


class LinearLogger:

    # Public

    def __init__(self):
        self.__stack = []

    def __call__(self, event):
        logger = logging.getLogger('task')
        if isinstance(event, CallTaskEvent):
            if event.state == event.INIT:
                self.__stack.append(event.task)
            elif event.state in [event.DONE, event.FAIL]:
                prefix = '[+] '
                style = 'done'
                if event.state == event.FAIL:
                    prefix = '[-] '
                    style = 'fail'
                message = ''
                message += prefix
                message += self.__format_stack(self.__stack)
                message += pack(*event.args, **event.kwargs)
                message = sformat(message, style, settings.styles)
                logger.info(message)
                self.__stack.pop()

    def __repr__(self):
        return '<LinearLogger>'

    # Private

    def __format_stack(self, stack):
        names = []
        for task in stack:
            if task.meta_qualname:
                names.append(task.meta_qualname)
        result = '/'.join(names)
        return result
