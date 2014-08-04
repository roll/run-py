from box.functools import cachedproperty
from ..cluster import Cluster
from ..signal import Dispatcher
from ..task import Task
from .controller import Controller
from .stack import Stack

class Machine:

    # Public

    def __init__(self, *,
                 names=None, tags=None,
                 file=None, exclude=None,
                 basedir=None, recursively=False,
                 grayscale=False, skip=False, plain=False,
                 **find_params):
        self._names = names
        self._tags = tags
        self._file = file
        self._exclude = exclude
        self._basedir = basedir
        self._recursively = recursively
        self._grayscale = grayscale
        self._skip = skip
        self._plain = plain
        self._find_params = find_params

    def process(self, task, *args, **kwargs):
        self._controller.listen()
        tasks = getattr(self._cluster, task)
        for task in tasks:
            if isinstance(task, self._task_class):
                result = task(*args, **kwargs)
                if result:
                    self._print(result)
            else:
                self._print(task)

    # Protected

    _cluster_class = Cluster
    _controller_class = Controller
    _dispatcher_class = Dispatcher
    _print = staticmethod(print)
    _stack_class = Stack
    _task_class = Task

    @cachedproperty
    def _controller(self):
        return self._controller_class(
            self._dispatcher, self._stack)

    @cachedproperty
    def _cluster(self):
        return self._cluster_class(
            names=self._names,
            tags=self._tags,
            file=self._file,
            exclude=self._exclude,
            basedir=self._basedir,
            recursively=self._recursively,
            grayscale=self._grayscale,
            skip=self._skip,
            dispatcher=self._dispatcher,
            **self._find_params)

    @cachedproperty
    def _dispatcher(self):
        return self._dispatcher_class()

    @cachedproperty
    def _stack(self):
        if not self._plain:
            return self._stack_class()
        else:
            return None
