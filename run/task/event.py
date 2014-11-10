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

    INIT = 'init'
    DONE = 'done'
    FAIL = 'fail'

    # TODO: add async flag?
    def __init__(self, __task, __state, *args, **kwargs):
        super().__init__(__task)
        self.__state = __state
        self.__args = args
        self.__kwargs = kwargs

    @property
    def state(self):
        return self.__state

    @property
    def args(self):
        return self.__args

    @property
    def kwargs(self):
        return self.__kwargs
