import inspect
from .task import Task


class DescriptorTask(Task):

    # Public

    def __init__(self, descriptor):
        self.__descriptor = descriptor

    def meta_invoke(self):
        return self.__descriptor.__get__(
            self.meta_module, type(self.meta_module))

    @property
    def meta_docstring(self):
        return self._meta_get_parameter(
            'docstring',
            inherit=False,
            default=str(inspect.getdoc(self.__descriptor)).strip())
