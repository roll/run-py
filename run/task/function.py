import re
import inspect
from .task import Task


class FunctionTask(Task):

    # Public

    def __init__(self, function, *args, bind=False, **kwargs):
        self.__function = function
        self.__bind = bind
        super().__init__(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            name='docstring', lookup=True,
            default=str(inspect.getdoc(self.__function)).strip())

    def meta_invoke(self, *args, **kwargs):
        if self.__bind:
            args = [self.meta_module] + list(args)
        return self.__function(*args, **kwargs)

    @property
    def meta_signature(self):
        signature = str(inspect.signature(self.__function))
        if self.__bind:
            signature = re.sub('self[,\s]*', '', signature)
        return self.meta_inspect(
            name='signature', lookup=True, default=signature)
