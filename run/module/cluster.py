import os
import inspect
from ..find import find
from .module import Module


class ClusterModule(Module):

    # Public

    def __init__(self, *args, **kwargs):
        basedir = kwargs.pop('basedir', None)
        notfilepath = os.path.relpath(
            inspect.getfile(type(self.meta_module)), start=basedir)
        Modules = self._find(
            target=self._Module,
            key=kwargs.pop('key', None),
            tags=kwargs.pop('tags', None),
            file=kwargs.pop('file', None),
            basedir=basedir,
            recursively=kwargs.pop('recursively', None),
            filters=[{'notfilepath': notfilepath}])
        return Modules

    # Protected

    _find = find
    _Module = Module
