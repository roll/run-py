import os
from box.findtools import find_objects
from box.functools import Function, cachedproperty
from ..module import Module
from ..settings import settings
from .common import CommonConstraint
from .meta import MetaConstraint
from .not_found import NotFound

class find(Function):
    """Find run modules.
    """

    # Public

    default_basedir = settings.basedir
    default_exclude = settings.exclude
    default_file = settings.file
    default_names = settings.names
    default_recursively = settings.recursively
    default_tags = settings.tags

    def __init__(self, names=None, tags=None, *,
                 file=None, exclude=None, basedir=None, recursively=None,
                 **find_params):
        if names is None:
            names = self.default_names
        if tags is None:
            tags = self.default_tags
        if file is None:
            file = self.default_file
        if exclude is None:
            exclude = self.default_exclude
        if basedir is None:
            basedir = self.default_basedir
        if recursively is None:
            recursively = self.default_recursively
        self._names = names
        self._tags = tags
        self._file = file
        self._exclude = exclude
        self._basedir = basedir
        self._recursively = recursively
        self._find_params = find_params

    def __call__(self):
        module_classes = self._find_objects(
            basedir=self._basedir,
            filename=self._filename,
            notfilename=self._notfilename,
            filepath=self._filepath,
            notfilepath=self._notfilepath,
            maxdepth=self._maxdepth,
            mappers=self._mappers,
            getfirst_exception=self._getfirst_exception,
            **self._find_params)
        return module_classes

    # Protected

    _getfirst_exception = NotFound
    _find_objects = find_objects
    _module_class = Module

    @property
    def _filename(self):
        if self._file:
            if os.path.sep not in self._file:
                return self._file
        return None

    @property
    def _filepath(self):
        if self._file:
            if os.path.sep in self._file:
                return self._file
        return None

    @property
    def _notfilename(self):
        if self._exclude:
            if os.path.sep not in self._exclude:
                return self._exclude
        return None

    @property
    def _notfilepath(self):
        if self._exclude:
            if os.path.sep in self._exclude:
                return self._exclude
        return None

    @property
    def _maxdepth(self):
        if not self._recursively:
            return 1
        return None

    @cachedproperty
    def _mappers(self):
        mappers = []
        common = CommonConstraint(self._module_class)
        if common:
            mappers.append(common)
        meta = MetaConstraint(self._names, self._tags)
        if meta:
            mappers.append(meta)
        return mappers
