from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttribute
from ..dispatcher import dispatcher
from .signal import InitiatedVarSignal, RetrievedVarSignal

class Var(DependentAttribute, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        self._dispatcher.add_signal(InitiatedVarSignal(self))
        self._resolve_requirements()
        result = self.retrieve()
        self._process_triggers()
        self.dispatcher.add_signal(RetrievedVarSignal(self))
        return result
 
    def __set__(self, module, value):
        self.retrieve = lambda self: value
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
    #Protected
    
    _dispatcher = dispatcher    