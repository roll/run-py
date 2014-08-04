import inspect
from .task import Task

class DescriptorTask(Task):

    # Public

    def __init__(self, descriptor):
        self._descriptor = descriptor

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', str(inspect.getdoc(self._descriptor)).strip())

    def meta_invoke(self):
        return self._descriptor.__get__(
            self.meta_module, type(self.meta_module))
