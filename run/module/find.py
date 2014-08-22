import os
import inspect
from ..find import find
from .module import Module


class FindModule(Module):

    # Public

    @classmethod
    def __meta_create__(cls, *, meta_module, meta_updates,
                        key=None, tags=None,
                        file=None, exclude=None, basedir=None, recursively=None):
        notfilepath = os.path.relpath(
            inspect.getfile(type(meta_module)), start=basedir)
        Module = cls._find(
            target=cls._Module,
            key=key,
            tags=tags,
            file=file,
            basedir=basedir,
            recursively=recursively,
            filters=[{'notfilepath': notfilepath}],
            getfirst=True)
        module = Module(
            meta_module=meta_module,
            meta_updates=meta_updates)
        return module

    # Protected

    _find = find
    _Module = Module
