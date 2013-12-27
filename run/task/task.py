from ..dependent import DependentAttribute
from ..dispatcher import dispatcher
from .signal import RequestedTaskSignal, CompletedTaskSignal

class Task(DependentAttribute):
    
    #Public
    
    def __get__(self, module, module_class=None):
        return self
    
    def __call__(self, *args, **kwargs):
        with dispatcher.register(self):
            dispatcher.add_signal(RequestedTaskSignal(self))
            self._resolve_requirements()
            result = self.complete(*args, **kwargs)
            self._process_triggers()
            dispatcher.add_signal(CompletedTaskSignal(self))
            return result
    
    def complete(self, *args, **kwargs):
        pass