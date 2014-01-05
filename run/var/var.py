from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttribute
from .signal import InitiatedVarSignal, RetrievedVarSignal

#TODO: add caching! (here or in concrete vars?)
class Var(DependentAttribute, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        self.meta_dispatcher.add_signal(
            self._initiated_signal_class(self))
        self._resolve_requirements()
        result = self.retrieve()
        self._process_triggers()
        self.meta_dispatcher.add_signal(
            self._retrieved_signal_class(self))
        return result
 
    def __set__(self, module, value):
        self.retrieve = lambda: value
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
    #Protected
    
    _initiated_signal_class = InitiatedVarSignal
    _retrieved_signal_class = RetrievedVarSignal