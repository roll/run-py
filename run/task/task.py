from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttribute
from .signal import InitiatedTaskSignal, CompletedTaskSignal

class Task(DependentAttribute, metaclass=ABCMeta):
    
    #Public
    
    def __get__(self, module, module_class=None):
        return self
    
    def __set__(self, module, value):
        if callable(value):
            self.complete = value
        else:
            raise TypeError(
            'Attribute "{name}" is task "{task}" and '
            'can be set only to callable value'.
            format(name=self.meta_name, task=self))
    
    def __call__(self, *args, **kwargs):
        self.meta_dispatcher.add_signal(
            self._initiated_signal_class(self))
        self._resolve_requirements()
        result = self.complete(*args, **kwargs)
        self._process_triggers()
        self.meta_dispatcher.add_signal(
            self._retrieved_signal_class(self))
        return result
    
    @abstractmethod
    def complete(self, *args, **kwargs):
        pass #pragma: no cover
    
    #Protected
    
    _initiated_signal_class = InitiatedTaskSignal
    _retrieved_signal_class = CompletedTaskSignal    