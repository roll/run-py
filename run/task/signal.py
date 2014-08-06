from ..signal import Signal


class TaskSignal(Signal):

    # Public

    def __init__(self, task):
        self._task = task

    @property
    def task(self):
        return self._task


class InitiatedTaskSignal(TaskSignal): pass
class SuccessedTaskSignal(TaskSignal): pass
class FailedTaskSignal(TaskSignal): pass
