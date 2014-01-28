from .var import Var

class TaskVar(Var):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        self._is_builtin = kwargs.pop('is_builtin', False)
        
    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        self._args = args
        self._kwargs = kwargs
 
    def retrieve(self):
        if self._is_builtin:
            #Complete without resolving requirements, triggers
            result = self._task.complete(*self._args, **self._kwargs)
        else:
            result = self._task(*self._args, **self._kwargs)
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
        if self._is_builtin:
            #Rebuild task with rebase on own module
            task = task.meta_builder(module=self.meta_module)
        return task