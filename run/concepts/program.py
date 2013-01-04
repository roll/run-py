from abc import ABCMeta, abstractmethod

class Program(object):
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def process(self): 
        pass #pragma: no cover