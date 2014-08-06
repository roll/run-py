from .dispatcher import Dispatcher


class NullDispatcher(Dispatcher):

    # Public

    def __bool__(self):
        return False

    def add_handler(self, handler): pass
    def add_signal(self, signal): pass
