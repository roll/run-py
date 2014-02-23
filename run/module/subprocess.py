from .module import Module
from ..task import SubprocessTask

class SubprocessModule(Module):

    #Public

    def __init__(self, mapping={}, prefix='', separator=' '):
        mapping = self._default_mapping
        mapping.update(mapping)
        for task_name, task_prefix in mapping.items():
            if not hasattr(type(self), task_name):
                eprefix = separator.join(filter(None, [prefix, task_prefix]))
                task = SubprocessTask(eprefix, separator, module=self)
                setattr(type(self), task_name, task)        
        
    #Protected
    
    _default_mapping = {} 