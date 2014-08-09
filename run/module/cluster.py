import logging
from box.functools import cachedproperty
from .find import find


class ModuleCluster:
    """Modules cluster representation.
    """

    # Public

    def __init__(self, *filters,
                 names=None, tags=None,
                 file=None, basedir=None, recursively=False,
                 grayscale=False, skip=False, dispatcher=None,
                 **params):
        self._filters = filters
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        self._grayscale = grayscale
        self._skip = skip
        self._dispatcher = dispatcher
        self._params = params

    def __getattr__(self, name):
        tasks = []
        for module in self._modules:
            try:
                task = getattr(module, name)
                tasks.append(task)
            except AttributeError as exception:
                if self._skip:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))
                else:
                    raise
        return tasks

    # Protected

    _find = staticmethod(find)

    @cachedproperty
    def _modules(self):
        modules = []
        for Module in self._Modules:
            module = Module(
                meta_grayscale=self._grayscale,
                meta_dispatcher=self._dispatcher,
                meta_module=None)
            modules.append(module)
        return modules

    @cachedproperty
    def _Modules(self):
        Modules = self._find(
            *self._filters,
            names=self._names,
            tags=self._tags,
            file=self._file,
            basedir=self._basedir,
            recursively=self._recursively,
            **self._params)
        return Modules
