import inspect
from .var import Var


class DescriptorVar(Var):

    # Public

    def __init__(self, descriptor):
        self.__descriptor = descriptor

    @property
    def Docstring(self):
        default = str(inspect.getdoc(self.__descriptor)).strip()
        return self.Inspect('Docstring', default=default)

    def Invoke(self):
        return self.__descriptor.__get__(
            self.Module, type(self.Module))
