from ..dependent import DependentAttribute
from ..dispatcher import dispatcher

class Task(DependentAttribute):
    
    #Public
    
    def __get__(self, module, module_class=None):
        return self
    
    def __call__(self, *args, **kwargs):
        with dispatcher.register(self):
            self._resolve_requirements()
            result = self.complete(*args, **kwargs)
            self._process_triggers()
            return result
    
    def complete(self, *args, **kwargs):
        pass