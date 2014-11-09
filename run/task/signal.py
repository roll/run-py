class Signal:

    # Public

    pass


class TaskSignal(Signal):

    # Public

    def __init__(self, task):
        self.__task = task

    @property
    def task(self):
        return self.__task


class CallTaskSignal(TaskSignal):

    # Public

    def __init__(self, task, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs
        super().__init__(task)

    @property
    def args(self):
        return self.__args

    @property
    def kwargs(self):
        return self.__kwargs


class DoneTaskSignal(TaskSignal):

    # Public

    pass


class FailTaskSignal(TaskSignal):

    # Public

    pass
