from .task import Task

class DerivedTask(Task):

    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        super().__init__(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self._meta_params.get('docstring', 
            'Derived from task "{task_qualname}".\n{task_docstring}'.
            format(task_qualname=self._task.meta_qualname,
                   task_docstring=self._task.meta_docstring))         
     
    @property
    def meta_signature(self):
        return self._meta_params.get('signature', 
            self._task.meta_signature)        

    def invoke(self, *args, **kwargs):
        return self._task(*args, **kwargs)
    
    #Protected
    
    @property
    def _task(self):
        task = getattr(self.meta_module, self._task_name)
        if not callable(task):
            raise TypeError(
                    'Attribute to derive from "{task_name}" '
                    'must be a Task or a callable object.'.
                format(task_name=self._task_name))
        return task