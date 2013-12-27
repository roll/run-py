from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttribute
from ..dispatcher import dispatcher

class Var(DependentAttribute, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        with dispatcher.register(self):
            self._resolve_requirements()
            result = self.retrieve()
            self._process_triggers()
            return result
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
    
    
        