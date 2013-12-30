from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttribute
from ..dispatcher import dispatcher
from .signal import InitiatedVarSignal, RetrievedVarSignal

class Var(DependentAttribute, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        self._dispatcher.add_signal(
            self._initiated_signal_class(self))
        self._resolve_requirements()
        result = self.retrieve()
        self._process_triggers()
        self._dispatcher.add_signal(
            self._retrieved_signal_class(self))
        return result
 
    def __set__(self, module, value):
        self.retrieve = lambda: value
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
    #Protected
    
    _dispatcher = dispatcher
    _initiated_signal_class = InitiatedVarSignal
    _retrieved_signal_class = RetrievedVarSignal