from copy import copy
from .task import Task

class PartialTask(Task):

    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        self._is_builtin = kwargs.pop('is_builtin', False)

    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        self._args = args
        self._kwargs = kwargs
    
    def invoke(self, *args, **kwargs):
        eargs = self._args+args
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        if self._is_builtin:
            #Invoke without resolving requirements, triggers
            result = self._task.invoke(*eargs, **ekwargs)
        else:
            result = self._task(*eargs, **ekwargs)
        return result
        
    @property
    def meta_signature(self):
        return self._task.meta_signature

    @property
    def meta_docstring(self):
        return self._task.meta_docstring
    
    @property
    def _task(self):
        task = getattr(self.meta_module, self._task_name)
        if self._is_builtin:
            #Rebuild task with rebase on own module
            task = task.meta_builder(module=self.meta_module)
        return task