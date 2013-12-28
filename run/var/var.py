from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttribute
from ..dispatcher import dispatcher
from .signal import InitiatedVarSignal, RetrievedVarSignal

class Var(DependentAttribute, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        dispatcher.add_signal(InitiatedVarSignal(self))
        self._resolve_requirements()
        result = self.retrieve()
        self._process_triggers()
        dispatcher.add_signal(RetrievedVarSignal(self))
        return result
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
    
    
        