from .var import Var

class TaskVar(Var):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        self._args = args
        self._kwargs = kwargs
 
    def retrieve(self):
        return self._task(*self._args, **self._kwargs)
        
    #TODO: implement for var
    @property
    def meta_signature(self):
        return self._task.meta_signature

    #TODO: implement for var    
    @property    
    def meta_docstring(self):
        return self._task.meta_docstring
    
    #Protected
    
    @property
    def _task(self):
        return getattr(self.meta_module, self._task_name)