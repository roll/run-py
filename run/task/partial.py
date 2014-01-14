from .task import Task

class PartialTask(Task):

    #Public

    def __init__(self, task_name, *args, **kwargs):
        self._task_name = task_name
        self._args = args
        self._kwargs = kwargs
    
    def complete(self, *args, **kwargs):
        eargs = self._args+args
        ekwargs = self._kwargs
        ekwargs.update(kwargs) 
        return self._task(*eargs, **ekwargs)
        
    #TODO: implement for partial
    @property
    def meta_signature(self):
        return self._task.meta_signature

    #TODO: implement for partial    
    @property    
    def meta_docstring(self):
        return self._task.meta_docstring
    
    #Protected
    
    @property
    def _task(self):
        return getattr(self.meta_module, self._task)