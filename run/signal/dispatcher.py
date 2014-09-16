class Dispatcher:

    # Public

    def __init__(self):
        self.__handlers = []

    def __repr__(self):
        return '<Dispatcher>'

    def add_handler(self, handler):
        self.__handlers.append(handler)

    def add_signal(self, signal):
        for handler in self.__handlers:
            handler.handle(signal)
