import logging
from ..dependent import DependentAttribute

class Task(DependentAttribute):
    
    #Public
    
    def __get__(self, module, module_class=None):
        return self
    
    def __call__(self, *args, **kwargs):
        self._resolve_requirements()
        #TODO: add error handling?
        result = self.complete(*args, **kwargs)
        self._process_triggers()
        self.meta_logger.info('Task completed')
        return result
    
    def complete(self, *args, **kwargs):
        pass