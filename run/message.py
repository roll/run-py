from abc import ABCMeta, abstractmethod

class Message(metaclass=ABCMeta):
    
    #Public
    
    @property
    def protocol(self):
        return 'run-json-1.0'
    
    @property
    @abstractmethod
    def content(self):
        pass #pragma: no cover