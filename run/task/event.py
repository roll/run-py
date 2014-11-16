import time


class Event:

    # Public

    def __init__(self):
        self.__time = time.time()

    @property
    def time(self):
        return self.__time


class TaskEvent(Event):

    # Public

    def __init__(self, task):
        self.__task = task
        super().__init__()

    @property
    def task(self):
        return self.__task


class CallTaskEvent(TaskEvent):

    # Public

    INIT = 'init'
    DONE = 'done'
    FAIL = 'fail'

    def __init__(self, __task, __state, *args, **kwargs):
        self.__state = __state
        self.__args = args
        self.__kwargs = kwargs
        super().__init__(__task)

    @property
    def state(self):
        return self.__state

    @property
    def args(self):
        return self.__args

    @property
    def kwargs(self):
        return self.__kwargs
