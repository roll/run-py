class Dispatcher:

    # Public

    def __init__(self):
        self._handlers = []

    def __repr__(self):
        return '<Dispatcher>'

    def add_handler(self, handler):
        self._handlers.append(handler)

    def add_signal(self, signal):
        for handler in self._handlers:
            handler.handle(signal)
