import re
import inspect
from .task import Task


class MethodTask(Task):

    # Public

    def __init__(self, method):
        self.__method = method

    @property
    def Docstring(self):
        return self.Inspect(
            'Docstring', default=str(inspect.getdoc(self.__method)).strip())

    def Invoke(self, *args, **kwargs):
        return self.__method(self.Module, *args, **kwargs)

    @property
    def Signature(self):
        default = str(inspect.signature(self.__method))
        default = re.sub('self[,\s]*', '', default)
        return self.Inspect('Signature', default=default)
