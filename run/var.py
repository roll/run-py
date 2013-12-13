from abc import ABCMeta, abstractmethod
from .property import Property

class Var(Property, metaclass=ABCMeta):
    
    #Public

    def __get__(self, run, runclass=None):
        self._run = run
        if '_value' not in self.__dict__:
            self._value = self.retrieve()
        return self._value
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
    def reset(self):
        del self._value
        
        
class PlainVar(Var):
    
    def __init__(self, plain_value, **kwargs):
        super().__init__(**kwargs)
        self._plain_value = plain_value
 
    def retrieve(self):
        return self._plain_value    