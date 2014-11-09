import logging
from ..helpers import sformat
from ..task import CallTaskSignal, DoneTaskSignal, FailTaskSignal
from ..settings import settings  # @UnusedImport


class Controller:

    # Public

    def __init__(self, *, compact=settings.compact, plain=settings.plain):
        self.__compact = compact
        self.__plain = plain
        self.__stack = []

    def __call__(self, signal):
        # Stack operations
        if self.__compact:
            # TODO: stack here is not tread-safe?
            self.__stack.append(signal.task)
            formatted_stack = self.__format_stack(self.__stack)
            self.__stack.pop()
        else:
            if isinstance(signal, CallTaskSignal):
                self.__stack.append(signal.task)
            formatted_stack = self.__format_stack(self.__stack)
            if isinstance(signal, (DoneTaskSignal, FailTaskSignal)):
                self.__stack.pop()
        # Logging operations
        formatted_signal = self.__format_signal(signal)
        if formatted_signal:
            message = formatted_signal + formatted_stack
            logger = logging.getLogger('task')
            logger.info(message)

    # Private

    def __format_stack(self, stack):
        names = []
        if len(stack) >= 1:
            previous = self.__stack[0]
            name = previous.meta_qualname
            if not self.__plain:
                name = sformat(name, previous.meta_style, settings.styles)
            names.append(name)
            for task in stack[1:]:
                current = task
                if current.meta_module == previous.meta_module:
                    name = current.meta_name
                    if not self.__plain:
                        name = sformat(name, current.meta_style, settings.styles)
                    names.append(name)
                else:
                    name = current.meta_qualname
                    if not self.__plain:
                        name = sformat(name, current.meta_style, settings.styles)
                    names.append(name)
                previous = current
        return '/'.join(filter(None, names))

    def __format_signal(self, signal):
        result = '[+] '  # TODO: fix
        return result
