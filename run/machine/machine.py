import logging
from box.functools import cachedproperty
from ..module import ModuleCluster
from ..signal import Dispatcher, CallbackHandler
from ..task import Task, TaskSignal
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
        self._init_handlers()

    def process(self, task, *args, **kwargs):
        tasks = getattr(self._cluster, task)
        for task in tasks:
            if isinstance(task, self._Task):
                result = task(*args, **kwargs)
                if result:
                    self._print(result)
            else:
                self._print(task)

    # Protected

    _CallbackHandler = CallbackHandler
    _Dispatcher = Dispatcher
    _ModuleCluster = ModuleCluster
    _print = staticmethod(print)
    _Stack = Stack
    _Task = Task
    _TaskSignal = TaskSignal

    def _init_handlers(self):
        self._dispatcher.add_handler(
            self._CallbackHandler(
                self._on_task_signal,
                signals=[self._TaskSignal]))

    # TODO: improve design?
    def _on_task_signal(self, signal):
        if signal.event == 'initiated':
            if not self._compact:
                self._stack.push(signal.task)
        elif signal.event in ['successed', 'failed']:
            if self._compact:
                self._stack.push(signal.task)
            message = signal.format(signal.prefix) + repr(self._stack)
            logger = logging.getLogger('task')
            logger.info(message)
            self._stack.pop()

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
        return self._Stack()
