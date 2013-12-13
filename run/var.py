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
        
        
class ValueTask(Var):
    
    def __init__(self, default_value, **kwargs):
        super().__init__(**kwargs)
        self._default_value = default_value
 
    def retrieve(self):
        return self._default_value    