from .task import Task

class DerivedTask(Task):

    # Public

    def __init__(self, task, *args, **kwargs):
        self._task = task
        super().__init__(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self._meta_params.get('docstring',
            'Derived from task "{task_qualname}".\n{task_docstring}'.
            format(task_qualname=self._task_instance.meta_qualname,
                   task_docstring=self._task_instance.meta_docstring))

    def meta_invoke(self, *args, **kwargs):
        return self._task_instance(*args, **kwargs)

    @property
    def meta_signature(self):
        return self._meta_params.get('signature',
            self._task_instance.meta_signature)

    # Protected

    @property
    def _task_instance(self):
        return getattr(self.meta_module, self._task)
