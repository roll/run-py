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
    """Task call event.

    Parameters
    ----------
    task: :class:`.Task`
        Task object.
    uid: int
        Call unique identifier.
    state: str
        Call state: INIT, DONE or FAIL.
    args: tuple
        Call args.
    kwargs: dict
        Call kwargs.
    """

    # Public

    INIT = 'init'
    DONE = 'done'
    FAIL = 'fail'

    def __init__(self, task, *, uid, state, args=(), kwargs={}):
        self.__uid = uid
        self.__state = state
        self.__args = args
        self.__kwargs = kwargs
        super().__init__(task)

    @property
    def uid(self):
        return self.__uid

    @property
    def state(self):
        return self.__state

    @property
    def args(self):
        return self.__args

    @property
    def kwargs(self):
        return self.__kwargs
