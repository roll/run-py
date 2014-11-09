import logging


class Controller:

    # Public

    def __call__(self, signal):
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
