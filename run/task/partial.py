from .task import Task

class PartialTask(Task):

    #Public

    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        self._args = args
        self._kwargs = kwargs
    
    def complete(self, *args, **kwargs):
        eargs = self._args+args
        ekwargs = self._kwargs
        ekwargs.update(kwargs) 
        return self._task(*eargs, **ekwargs)
        
    @property
    def meta_signature(self):
        return self._task.meta_signature

    @property    
    def meta_docstring(self):
        return self._task.meta_docstring
    
    @property
    def _task(self):
        return getattr(self.meta_module, self._task_name)    