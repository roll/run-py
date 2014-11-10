import logging
from ..helpers import sformat
from ..task import CallTaskEvent
from ..settings import settings


class BriefLogger:

    # Public

    def __call__(self, event):
        logger = logging.getLogger('task')
        if isinstance(event, CallTaskEvent):
            if event.state in [event.DONE, event.FAIL]:
                prefix = '[+] '
                style = 'successed'
                if event.state == event.FAIL:
                    prefix = '[-] '
                    style = 'failed'
                message = ''
                message += prefix
                message += event.task.meta_qualname
                message = sformat(message, style, settings.styles)
                logger.info(message)

    def __repr__(self):
        return '<BriefLogger>'
