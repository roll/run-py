from box.terminal import Formatter
from ..settings import settings
from ..signal import Signal


class TaskSignal(Signal):

    # Public

    def __init__(self, task, *, event):
        self._task = task
        self._event = event

    @property
    def event(self):
        return self._event

    def format(self, text):
        result = text
        if not self.task.meta_plain:
            style = self._styles.get(self.event, None)
            if style is not None:
                formater = Formatter()
                result = formater.format(text, **style)
        return result

    @property
    def prefix(self):
        # TODO: move to settings
        if self.event == 'initiated':
            return '[.] '
        elif self.event == 'successed':
            return '[+] '
        elif self.event == 'failed':
            return '[-] '

    @property
    def task(self):
        return self._task

    # Protected

    _styles = settings.styles
