from .task import Task

class PartialTask(Task):

    #Public

    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
    
    def complete(self, *args, **kwargs):
        task = getattr(self.meta_module, self._task)
        eargs = self._args+args
        ekwargs = self._kwargs
        ekwargs.update(kwargs) 
        return task(*eargs, **ekwargs)
        
    #TODO: implement for partial
    @property
    def meta_signature(self):
        return self._task.meta_signature

    #TODO: implement for partial    
    @property    
    def meta_docstring(self):
        return self._task.meta_docstring