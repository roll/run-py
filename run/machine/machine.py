from box.functools import cachedproperty
from ..module import ModuleCluster
from ..signal import Dispatcher
from ..task import Task
from .controller import Controller
from .stack import Stack


class Machine:

    # Public

    def __init__(self, *,
                 names=None, tags=None,
                 file=None, basedir=None, recursively=False,
                 plain=False, skip=False, compact=False):
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        self._plain = plain
        self._skip = skip
        self._compact = compact

    def process(self, task, *args, **kwargs):
        self._controller.listen()
        tasks = getattr(self._cluster, task)
        for task in tasks:
            if isinstance(task, self._Task):
                result = task(*args, **kwargs)
                if result:
                    self._print(result)
            else:
                self._print(task)

    # Protected

    _ModuleCluster = ModuleCluster
    _Controller = Controller
    _Dispatcher = Dispatcher
    _print = staticmethod(print)
    _Stack = Stack
    _Task = Task

    @cachedproperty
    def _controller(self):
        return self._Controller(
            self._dispatcher, self._stack)

    @cachedproperty
    def _cluster(self):
        return self._ModuleCluster(
            names=self._names,
            tags=self._tags,
            file=self._file,
            basedir=self._basedir,
            recursively=self._recursively,
            plain=self._plain,
            skip=self._skip,
            dispatcher=self._dispatcher)

    @cachedproperty
    def _dispatcher(self):
        return self._Dispatcher()

    @cachedproperty
    def _stack(self):
        if not self._compact:
            return self._Stack()
        else:
            return None
