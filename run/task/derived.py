from .task import Task

class DerivedTask(Task):

    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        super().__init__(*args, **kwargs)

    def invoke(self, *args, **kwargs):
        return self._task(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self._meta_params.get('docstring', 
            'Task is derived from task "{task_qualname}".\n'
            'Task "{task_qualname}" has following docstring:\n'
            '{task_docstring}'.
            format(task_qualname=self._task.meta_qualname,
                   task_docstring=self._task.meta_docstring))         
     
    @property
    def meta_signature(self):
        return self._meta_params.get('signature', 
            '{qualname} > {task_signature}'.
            format(qualname=self.meta_qualname,
                   task_signature=self._task.meta_signature))        
    
    #Protected
    
    @property
    def _task(self):
        return getattr(self.meta_module, self._task_name)