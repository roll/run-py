import os
import inspect
from box import find as box_find
from ..find import find
from ..module import Module
from ..task import FunctionTask
from ..var import Var


class FindModule(Module):

    # Public

    @classmethod
    def __meta_create__(cls, *args, meta_module, meta_updates,
                        key=None, tags=None,
                        file=None, exclude=None, basedir=None, recursively=None,
                        **kwargs):
        notfilepath = os.path.relpath(
            inspect.getfile(type(meta_module)), start=basedir)
        Module = cls._find(
            target=cls._Module,
            key=key,
            tags=tags,
            file=file,
            exclude=exclude,
            basedir=basedir,
            recursively=recursively,
            filters=[{'notfilepath': notfilepath}],
            getfirst=True)
        module = Module(
            *args,
            meta_module=meta_module,
            meta_updates=meta_updates,
            **kwargs)
        return module

    # Protected

    _find = find
    _Module = Module


class FindTask(FunctionTask):

    # Public

    def __init__(self, *args, mode='strings', **kwargs):
        try:
            function = getattr(box_find, 'find_' + mode)
        except AttributeError:
            raise ValueError('Unsupported mode "{mode}".'.
                             format(mode=mode))
        super().__init__(function, *args, **kwargs)


class FindVar(Var, FindTask): pass
