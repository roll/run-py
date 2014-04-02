from .task import Task

class NestedTask(Task):

    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        super().__init__(*args, **kwargs)       

    def invoke(self, *args, **kwargs):
        return self._task(*args, **kwargs)
        
    @property
    def meta_signature(self):
        return self._task.meta_signature

    @property
    def meta_docstring(self):
        return self._task.meta_docstring
    
    #Protected
    
    @property
    def _task(self):
        return getattr(self.meta_module, self._task_name)