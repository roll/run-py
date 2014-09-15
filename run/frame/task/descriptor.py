import inspect
from .task import Task


class DescriptorTask(Task):

    # Public

    # TODO: why args, kwargs?
    def __init__(self, descriptor, *args, **kwargs):
        self._descriptor = descriptor
        super().__init__(*args, **kwargs)

    def meta_invoke(self):
        return self._descriptor.__get__(
            self.meta_module, type(self.meta_module))

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', str(inspect.getdoc(self._descriptor)).strip())
