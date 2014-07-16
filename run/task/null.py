from .task import Task

class NullTask(Task):

    # Public

    @property
    def meta_docstring(self):
        return self._meta_params.get('docstring',
            'Do nothing but resolve dependencies.')

    def invoke(self):
        pass
