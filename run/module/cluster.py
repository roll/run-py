import logging
from box.functools import cachedproperty
from ..find import find
from .module import Module


class ModuleCluster:
    """Modules cluster representation.
    """

    # Public

    def __init__(self, *,
                 key=None, tags=None,
                 file=None, basedir=None, recursively=False,
                 plain=False, skip=False, dispatcher=None):
        self._key = key
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        self._plain = plain
        self._skip = skip
        self._dispatcher = dispatcher

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

    _find = find

    @cachedproperty
    def _modules(self):
        modules = []
        for Module in self._Modules:
            module = Module(
                meta_plain=self._plain,
                meta_dispatcher=self._dispatcher,
                meta_module=None)
            modules.append(module)
        return modules

    @cachedproperty
    def _Modules(self):
        Modules = self._find(
            key=self._key,
            tags=self._tags,
            file=self._file,
            basedir=self._basedir,
            recursively=self._recursively)
        return Modules


class ClusterModule(Module):

    # Public

    pass
