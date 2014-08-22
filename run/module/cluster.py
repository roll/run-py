import os
import inspect
from box.functools import cachedproperty
from ..find import find
from .module import Module


class ClusterModule(Module):

    # Public

    def __init__(self, *args,
                 key=None, tags=None,
                 file=None, exclude=None, basedir=None, recursively=None,
                 **kwargs):
        self._key = key
        self._tags = tags
        self._file = file
        self._exclude = exclude
        self._basedir = basedir
        self._recursively = recursively
        super().__init__(*args, **kwargs)

    # Protected

    _find = find
    _Module = Module

    @cachedproperty
    def _modules(self):
        modules = []
        for Module in self._Modules:
            module = Module(
                meta_dispatcher=self.meta_dispatcher,
                meta_plain=self.meta_plain,
                meta_module=None)
            modules.append(module)
        return modules

    @cachedproperty
    def _Modules(self):
        Modules = self._find(
            target=self._Module,
            key=self._key,
            tags=self._tags,
            file=self._file,
            basedir=self._basedir,
            recursively=self._recursively,
            filters=[{'notfilepath': self._notfilepath}])
        return Modules

    @property
    def _notfilepath(self):
        notfilepath = os.path.relpath(
            inspect.getfile(type(self.meta_module)), start=self._basedir)
        return notfilepath
