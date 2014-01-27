from .task import Task

class PartialTask(Task):

    #Public

    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
    
    def complete(self, *args, **kwargs):
        eargs = self._args+args
        ekwargs = self._kwargs
        ekwargs.update(kwargs) 
        return self._base_task(*eargs, **ekwargs)
        
    @property
    def meta_signature(self):
        return self._base_task.meta_signature

    @property    
    def meta_docstring(self):
        return self._base_task.meta_docstring
    
    @property
    def _base_task(self):
        task = self.meta_module.meta_attributes[self._task]
        base_task = task.meta_builder()
        base_task.meta_module = self.meta_module
        return base_task  