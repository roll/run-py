from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, signal):
        pass  # pragma: no cover


class CallbackHandler(Handler):

    # Public

    def __init__(self, callback, signals=None):
        if signals is None:
            signals = []
        self.__callback = callback
        self.__signals = signals

    def handle(self, signal):
        if isinstance(signal, tuple(self.__signals)):
            self.__callback(signal)
