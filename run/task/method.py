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
            name='docstring', lookup=True,
            default=str(inspect.getdoc(self.__method)).strip())

    def meta_invoke(self, *args, **kwargs):
        return self.__method(self.meta_module, *args, **kwargs)

    @property
    def meta_signature(self):
        signature = str(inspect.signature(self.__method))
        signature = re.sub('self[,\s]*', '', signature)
        return self.meta_inspect(
            name='signature', lookup=True, default=signature)
