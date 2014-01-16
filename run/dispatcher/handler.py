from abc import ABCMeta, abstractmethod

class DispatcherHandler(metaclass=ABCMeta):
    
    @abstractmethod
    def handle(self, signal):
        pass #pragma: no cover


class DispatcherCallbackHandler(DispatcherHandler):
    
    #Public
    
    def __init__(self, callback, signals=[]):
        self._callback = callback
        self._signals = signals
        
    def handle(self, signal):
        if isinstance(signal, tuple(self._signals)):
            self._callback(signal)  