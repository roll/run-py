import logging
from ..task import TaskSignal
from .stack import Stack


class Controller:

    # Public

    def listen(self, module):
        if module.meta_is_main_module:
            self.__stack = Stack()
            self.__compact = module.meta_compact
            module.meta_dispatcher.add_handler(
                handler=self.__on_task_signal, signals=[TaskSignal])

    # Private

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
