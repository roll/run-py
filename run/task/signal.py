from ..signal import Signal

class TaskSignal(Signal):

    # Public

    def __init__(self, attribute):
        self._attribute = attribute

    @property
    def attribute(self):
        return self._attribute


class InitiatedTaskSignal(TaskSignal): pass
class SuccessedTaskSignal(TaskSignal): pass
class FailedTaskSignal(TaskSignal): pass
