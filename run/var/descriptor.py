import inspect
from .var import Var


class DescriptorVar(Var):

    # Public

    def __init__(self, descriptor):
        self.__descriptor = descriptor

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            name='docstring', lookup=True,
            default=str(inspect.getdoc(self.__descriptor)).strip())

    def meta_invoke(self):
        return self.__descriptor.__get__(
            self.meta_module, type(self.meta_module))