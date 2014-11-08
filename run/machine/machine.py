import os
import inspect
import logging
from builtins import print
from sugarbowl import cachedproperty
from ..helpers import load
from ..module import Module
from ..settings import settings  # @UnusedImport
from ..task import TaskSignal
from .stack import Stack


class Machine:
    """Machine representation.

    Parameters
    ----------
    filepath: str
        Path to runfile.
    compact: bool
        Do not use stack.
    plain: bool
        Do not use color formatting.
    """

    # Public

    def __init__(self, *,
                 filepath=settings.filename,
                 compact=settings.compact,
                 plain=settings.plain):
        self.__filepath = filepath
        self.__compact = compact
        self.__plain = plain

    def run(self, attribute=None, *args, **kwargs):
        """
        Run machine.
        """
        if attribute is None:
            attribute = self.__module
        else:
            attribute = getattr(self.__module, attribute)
        if not callable(attribute):
            print(attribute)
            return
        result = attribute(*args, **kwargs)
        if result is None:
            return
        if not isinstance(result, list):
            print(result)
            return
        for element in result:
            if element is not None:
                print(result)
                return

    # Private

    @cachedproperty
    def __module(self):
        # Create module
        module = self.__Module(
            meta_plain=self.__plain,
            meta_module=None)
        # Add handlers
        module.meta_dispatcher.add_handler(
            handler=self.__on_task_signal,
            signals=[TaskSignal])
        return module

    @cachedproperty
    def __Module(self):
        filepath = os.path.abspath(self.__filepath)
        module = load(filepath)
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

    def __on_task_signal(self, signal):
        # Stack operations
        if self.__compact:
            # TODO: stack here is not tread-safe?
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
