from abc import ABCMeta, abstractmethod

class Driver(object):
    
    __metaclass__ = ABCMeta

    def __init__(self, command):
        self._command = command
    
    @abstractmethod
    def process(self): 
        pass #pragma: no cover