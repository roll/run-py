import logging
from ..helpers import pack
from .event import CallTaskEvent
from .stylize import stylize


class Logger:

    # Public

    def __call__(self, event):
        logger = logging.getLogger('task')
        if isinstance(event, CallTaskEvent):
            if event.state in [event.DONE, event.FAIL]:
                if event.task.meta_hidden:
                    return
                prefix = '[+] '
                style = 'done'
                if event.state == event.FAIL:
                    prefix = '[-] '
                    style = 'fail'
                message = ''
                message += prefix
                message += event.task.meta_qualname or '[top]'
                message += pack(*event.args, **event.kwargs)
                message = stylize(message, style=style)
                logger.info(message)

    def __repr__(self):
        return '<Logger>'
