import inspect
import logging
from builtins import print
from box.functools import cachedproperty
from importlib.machinery import SourceFileLoader
from ..module import Module
from ..settings import settings
from ..signal import Dispatcher, CallbackHandler
from ..task import TaskSignal
from .stack import Stack


class Machine:

    # Public

    default_filepath = settings.filepath
    default_compact = settings.compact
    default_plain = settings.plain

    def __init__(self, *, filepath=None, compact=False, plain=False):
        if filepath is None:
            filepath = self.default_filepath
        if compact is None:
            compact = self.default_compact
        if plain is None:
            plain = self.default_plain
        self.__filepath = filepath
        self.__compact = compact
        self.__plain = plain
        self.__init_handlers()

    def run(self, attribute=None, *args, **kwargs):
        if attribute is None:
            attribute = self.__module
        else:
            attribute = getattr(self.__module, attribute)
        if callable(attribute):
            result = attribute(*args, **kwargs)
            # TODO: is None?/bad work with ClusterModule
            if result:
                print(result)
        else:
            print(attribute)

    # Private

    def __init_handlers(self):
        self.__dispatcher.add_handler(
            CallbackHandler(self.__on_task_signal, signals=[TaskSignal]))

    @cachedproperty
    def __module(self):
        module = self.__Module(
            meta_dispatcher=self.__dispatcher,
            meta_plain=self.__plain,
            meta_module=None)
        return module

    @cachedproperty
    def __Module(self):
        loader = SourceFileLoader(self.__filepath, self.__filepath)
        module = loader.load_module(self.__filepath)
        for name in dir(module):
            attr = getattr(module, name)
            if not isinstance(attr, type):
                continue
            if not issubclass(attr, Module):
                continue
            if inspect.getmodule(attr) != module:
                continue
            return attr
        raise RuntimeError('Module not found.')

    @cachedproperty
    def __dispatcher(self):
        return Dispatcher()

    def __on_task_signal(self, signal):
        # Stack operations
        if self.__compact:
            # TODO: not tread-safe?
            self.__stack.push(signal.task)
            formatted__stack = self.__stack.format()
            self.__stack.pop()
        else:
            if signal.event == 'called':
                self.__stack.push(signal.task)
            formatted__stack = self.__stack.format()
            if signal.event in ['successed', 'failed']:
                self.__stack.pop()
        # Logging operations
        formatted_signal = signal.format()
        if formatted_signal:
            message = formatted_signal + formatted__stack
            logger = logging.getLogger('task')
            logger.info(message)

    @cachedproperty
    def __stack(self):
        return Stack()
