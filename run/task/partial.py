import inspect
from copy import copy
from .task import Task

class PartialTask(Task):

    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        self._is_expand = kwargs.pop('is_expand', True)
        self._is_merge = kwargs.pop('is_merge', False)

    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        self._args = args
        self._kwargs = kwargs
    
    def invoke(self, *args, **kwargs):
        eargs = self._args+args
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        if self._is_merge:
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
    
    #Protected
    
    @property
    def _task(self):
        task = getattr(self.meta_module, self._task_name)
        if self._is_merge:
            #Rebuild task with rebase on own module
            task = task.meta_builder(module=self.meta_module)
        return task
    
    def _expand(self, value):
        if inspect.isdatadescriptor(value):
            value = value.__get__(self.meta_module, type(self.meta_module))
        return value