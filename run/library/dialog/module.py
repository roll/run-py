from ...module import Module
from .var import DialogVar


# TODO: improve work
class DialogModule(Module):

    # Public

    def __init__(self, question='Please input "{name}": ', *args, **kwargs):
        self.__question = question
        self.__args = args
        self.__kwargs = kwargs

    def __getattr__(self, name):
        var = DialogVar(
            *self.__args,
            question=self.__question,
            name=name,
            meta_module=self,
            **self.__kwargs)
        setattr(type(self), name, var)
        result = getattr(self, name)
        return result

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            'docstring', inherit=False, default='DialogModule')
