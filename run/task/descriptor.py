import inspect
from .task import Task


class DescriptorTask(Task):

    # Public

    # TODO: why args, kwargs?
    def __init__(self, descriptor, *args, **kwargs):
        self.__descriptor = descriptor
        super().__init__(*args, **kwargs)

    def meta_invoke(self):
        return self.__descriptor.__get__(
            self.meta_module, type(self.meta_module))

    @property
    def meta_docstring(self):
        return self.meta_getmeta(
            'docstring',
            default=str(inspect.getdoc(self.__descriptor)).strip())
