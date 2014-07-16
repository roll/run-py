from box.dependency import inject
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
        module = self._module_class()
        return module

    # Protected

    _find = inject('find', module='run.cluster')

    @cachedproperty
    def _module_class(self):
        module_class = self._find(
            names=self._names,
            tags=self._tags,
            file=self._file,
            basedir=self._basedir,
            recursively=self._recursively,
            getfirst=True)
        return module_class
