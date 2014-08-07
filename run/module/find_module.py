from .module import Module
from .find import find


class FindModule(Module):

    # Public

    @classmethod
    def __meta_create__(cls, *args, meta_module, meta_updates, **kwargs):
        Module = cls._find(
            names=kwargs.pop('names', None),
            tags=kwargs.pop('tags', None),
            file=kwargs.pop('file', None),
            basedir=kwargs.pop('basedir', None),
            recursively=kwargs.pop('recursively', None),
            getfirst=True)
        module = Module(
            *args,
            meta_module=meta_module,
            meta_updates=meta_updates,
            **kwargs)
        return module

    # Protected

    _find = find
