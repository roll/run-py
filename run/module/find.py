from box.importlib import inject
from box.functools import Function, cachedproperty


class FindModule(Function):

    # Public

    def __init__(self, names=None, tags=None, *,
                file=None, basedir=None, recursively=False):
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively

    def __call__(self):
        module = self._Module()
        return module

    # Protected

    _find = inject('find', module='run.cluster')

    @cachedproperty
    def _Module(self):
        Module = self._find(
            names=self._names,
            tags=self._tags,
            file=self._file,
            basedir=self._basedir,
            recursively=self._recursively,
            getfirst=True)
        return Module
