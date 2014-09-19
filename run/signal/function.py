from .handler import Handler


class FunctionHandler(Handler):

    # Public

    def __init__(self, callback, signals=None):
        if signals is None:
            signals = []
        self.__callback = callback
        self.__signals = signals

    def handle(self, signal):
        if isinstance(signal, tuple(self.__signals)):
            self.__callback(signal)