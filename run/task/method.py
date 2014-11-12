import re
import inspect
from .task import Task


class MethodTask(Task):

    # Public

    def __init__(self, method):
        self.__method = method

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            'docstring', default=str(inspect.getdoc(self.__method)).strip())

    def meta_invoke(self, *args, **kwargs):
        return self.__method(self.meta_module, *args, **kwargs)

    @property
    def meta_signature(self):
        default = str(inspect.signature(self.__method))
        default = re.sub('self[,\s]*', '', default)
        return self.meta_inspect('signature', default=default)
