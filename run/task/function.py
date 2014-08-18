import inspect
from .task import Task


class FunctionTask(Task):

    # Public

    def __init__(self, function, *args, **kwargs):
        self._function = function
        super().__init__(*args, **kwargs)

    def meta_invoke(self, *args, **kwargs):
        return self._function(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', str(inspect.getdoc(self._function)).strip())

    @property
    def meta_signature(self):
        return self._meta_params.get(
            'signature', str(inspect.signature(self._function)))
