import re
import inspect
from .task import Task


class FunctionTask(Task):

    # Public

    # TODO: meta_bind instead of bind?
    def __init__(self, function, *args, bind=False, **kwargs):
        self.__function = function
        self.__bind = bind
        super().__init__(*args, **kwargs)

    def meta_invoke(self, *args, **kwargs):
        if self.__bind:
            args = [self.meta_module] + list(args)
        return self.__function(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', str(inspect.getdoc(self.__function)).strip())

    @property
    def meta_signature(self):
        signature = str(inspect.signature(self.__function))
        if self.__bind:
            signature = re.sub('self[,\s]*', '', signature)
        return self._meta_params.get('signature', signature)
