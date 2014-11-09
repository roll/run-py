class Signal:

    # Public

    pass


class TaskSignal(Signal):

    # Public

    def __init__(self, task, *, event):
        self.__task = task
        self.__event = event

    @property
    def task(self):
        return self.__task

    @property
    def event(self):
        return self.__event
