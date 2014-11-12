import logging
from ..helpers import pack
from ..task import CallTaskEvent
from ..utils import stylize


class LinearLogger:

    # Public

    def __init__(self):
        self.__stack = []

    def __call__(self, event):
        logger = logging.getLogger('task')
        if isinstance(event, CallTaskEvent):
            if event.state == event.INIT:
                self.__stack.append(event)
            elif event.state in [event.DONE, event.FAIL]:
                init = self.__stack[-1]
                time = (event.time - init.time) * 1000
                prefix = '[+] '
                style = 'done'
                if event.state == event.FAIL:
                    prefix = '[-] '
                    style = 'fail'
                message = ''
                message += prefix
                message += '[{time:.2f} ms] '.format(time=time)
                message += self.__format_stack(self.__stack)
                message += pack(*event.args, **event.kwargs)
                message = stylize(message, style=style)
                logger.info(message)
                self.__stack.pop()

    def __repr__(self):
        return '<LinearLogger>'

    # Private

    def __format_stack(self, stack):
        names = []
        for event in stack:
            if event.task.meta_qualname:
                names.append(event.task.meta_qualname)
        result = '/'.join(names)
        return result
