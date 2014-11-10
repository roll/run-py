class Event:

    # Public

    pass


class TaskEvent(Event):

    # Public

    def __init__(self, task):
        self.__task = task

    @property
    def task(self):
        return self.__task


class CallTaskEvent(TaskEvent):

    # Public

    # TODO: add async flag?
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


class DoneTaskEvent(TaskEvent):

    # Public

    pass


class FailTaskEvent(TaskEvent):

    # Public

    pass
