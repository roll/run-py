import logging
from box.functools import cachedproperty
from ..find import find
from ..module import Module
from ..signal import Dispatcher, CallbackHandler
from ..task import TaskSignal
from .stack import Stack


class Machine:

    # Public

    # TODO: add defaults from settings?
    def __init__(self, *,
                 key=None, tags=None,
                 file=None, exclude=None, basedir=None, recursively=False,
                 compact=False, skip=False, plain=False):
        self._key = key
        self._tags = tags
        self._file = file
        self._exclude = exclude
        self._basedir = basedir
        self._recursively = recursively
        self._compact = compact
        self._skip = skip
        self._plain = plain
        self._init_handlers()

    def run(self, attribute=None, *args, **kwargs):
        for module in self._modules:
            try:
                instance = module
                if attribute is not None:
                    instance = getattr(module, attribute)
                if callable(instance):
                    result = instance(*args, **kwargs)
                    if result:
                        self._print(result)
                else:
                    self._print(instance)
            except AttributeError as exception:
                if self._skip:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))
                else:
                    raise

    # Protected

    _CallbackHandler = CallbackHandler
    _Dispatcher = Dispatcher
    _find = find
    _Module = Module
    _print = staticmethod(print)
    _Stack = Stack
    _TaskSignal = TaskSignal

    def _init_handlers(self):
        self._dispatcher.add_handler(
            self._CallbackHandler(
                self._on_task_signal,
                signals=[self._TaskSignal]))

    def _on_task_signal(self, signal):
        # Stack operations
        if self._compact:
            # TODO: not tread-safe?
            self._stack.push(signal.task)
            formatted_stack = self._stack.format()
            self._stack.pop()
        else:
            if signal.event == 'launched':
                self._stack.push(signal.task)
            formatted_stack = self._stack.format()
            if signal.event in ['successed', 'failed']:
                self._stack.pop()
        # Logging operations
        formatted_signal = signal.format()
        if formatted_signal:
            message = formatted_signal + formatted_stack
            logger = logging.getLogger('task')
            logger.info(message)

    @cachedproperty
    def _modules(self):
        modules = []
        for Module in self._Modules:
            module = Module(
                meta_dispatcher=self._dispatcher,
                meta_plain=self._plain,
                meta_module=None)
            modules.append(module)
        return modules

    @cachedproperty
    def _Modules(self):
        Modules = self._find(
            target=self._Module,
            key=self._key,
            tags=self._tags,
            file=self._file,
            exclude=self._exclude,
            basedir=self._basedir,
            recursively=self._recursively)
        return Modules

    @cachedproperty
    def _dispatcher(self):
        return self._Dispatcher()

    @cachedproperty
    def _stack(self):
        return self._Stack()
