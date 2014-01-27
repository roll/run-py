from .var import Var

class TaskVar(Var):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
 
    def retrieve(self):
        return self._base_task(*self._args, **self._kwargs)
        
    @property
    def meta_signature(self):
        return self._base_task.meta_signature

    @property    
    def meta_docstring(self):
        return self._base_task.meta_docstring
    
    #Protected
    
    @property
    def _base_task(self):
        task = self.meta_module.meta_attributes[self._task]
        base_task = task.meta_builder(module=self.meta_module)
        return base_task