from abc import ABCMeta
from ..task import Task
from .signal import InitiatedVarSignal, ProcessedVarSignal

class Var(Task, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        return self()
 
    def __set__(self, module, value):
        self.invoke = lambda: value
    
    #Protected
    
    _initiated_signal_class = InitiatedVarSignal
    _processed_signal_class = ProcessedVarSignal