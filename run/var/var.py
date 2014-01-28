from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttribute
from .signal import InitiatedVarSignal, ProcessedVarSignal

class Var(DependentAttribute, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        self.meta_dispatcher.add_signal(
            self._initiated_signal_class(self))
        self._resolve_requirements()
        result = self.retrieve()
        self._process_triggers()
        self.meta_dispatcher.add_signal(
            self._processed_signal_class(self))
        return result
 
    def __set__(self, module, value):
        self.retrieve = lambda: value
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
    #Protected
    
    _initiated_signal_class = InitiatedVarSignal
    _processed_signal_class = ProcessedVarSignal