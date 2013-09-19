from abc import ABCMeta, abstractmethod

class Message(metaclass=ABCMeta):
    
    #Public
    
    @property
    @abstractmethod
    def content(self):
        pass #pragma: no cover