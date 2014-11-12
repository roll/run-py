import logging
from ..helpers import pack
from ..task import CallTaskEvent
from ..utils import stylize


class BriefLogger:

    # Public

    def __call__(self, event):
        logger = logging.getLogger('task')
        if isinstance(event, CallTaskEvent):
            if event.state in [event.DONE, event.FAIL]:
                prefix = '[+] '
                style = 'done'
                if event.state == event.FAIL:
                    prefix = '[-] '
                    style = 'fail'
                message = ''
                message += prefix
                message += event.task.meta_qualname
                message += pack(*event.args, **event.kwargs)
                message = stylize(message, style=style)
                logger.info(message)

    def __repr__(self):
        return '<BriefLogger>'
