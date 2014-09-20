class Dispatcher:

    # Public

    def __init__(self):
        self.__handlers = []

    def __repr__(self):
        return '<Dispatcher>'

    def add_handler(self, handler, *, signals=None):
        self.__handlers.append((handler, signals))

    def add_signal(self, signal):
        for handler, signals in self.__handlers:
            if signals is not None:
                if not isinstance(signal, tuple(signals)):
                    continue
            handler(signal)
