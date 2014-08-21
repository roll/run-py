from box.terminal import Formatter
from ..settings import settings
from ..signal import Signal


class TaskSignal(Signal):

    # Public

    def __init__(self, task, *, event):
        self._task = task
        self._event = event

    def format(self):
        result = self._events.get(self.event, '')
        if result:
            if not self.task.meta_plain:
                style = self._styles.get(self.event, None)
                if style is not None:
                    formater = Formatter()
                    result = formater.format(result, **style)
        return result

    @property
    def event(self):
        return self._event

    @property
    def task(self):
        return self._task

    # Protected

    _events = settings.events
    _styles = settings.styles
