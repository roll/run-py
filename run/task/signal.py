from clyde import sformat
from ..settings import settings
from ..signal import Signal


class TaskSignal(Signal):

    # Public

    def __init__(self, task, *, event):
        self.__task = task
        self.__event = event

    def format(self):
        result = settings.events.get(self.event, '')
        if result:
            if not self.task.meta_colorless:
                style = settings.styles.get(self.event, None)
                if style is not None:
                    result = sformat(result, **style)
        return result

    @property
    def task(self):
        return self.__task

    @property
    def event(self):
        return self.__event
