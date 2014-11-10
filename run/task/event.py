class Event:

    # Public

    pass


class TaskEvent(Event):

    # Public

    def __init__(self, __task):
        self.__task = __task

    @property
    def task(self):
        return self.__task


class CallTaskEvent(TaskEvent):

    # Public

    # TODO: add async flag?
    def __init__(self, __task, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs
        super().__init__(__task)

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
