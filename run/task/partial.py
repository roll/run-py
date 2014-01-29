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
        eargs = copy(self._args)
        eargs = eargs+args
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        if self._is_expand:
            eargs = self._expand(eargs)
            ekwargs = self._expand(ekwargs)   
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
    
    def _expand(self, args):
        try:
            iterator = args.items()
            result = {}            
        except AttributeError:
            iterator = enumerate(args)
            result = [None]*len(args)            
        for key, value in iterator:
            result[key] = self._expand_value(value)
        result = type(args)(result)
        return result                 
    
    def _expand_value(self, value):
        if inspect.isdatadescriptor(value):
            value = value.__get__(self.meta_module, type(self.meta_module))
        return value