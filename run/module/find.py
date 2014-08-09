import os
from box.findtools import find_objects
from box.functools import Function, cachedproperty
from ..settings import settings
from .constraint import Constraint
from .module import Module
from .not_found import NotFound


class find(Function):
    """Find run modules.
    """

    # Public

    default_basedir = settings.basedir
    default_file = settings.file
    default_names = settings.names
    default_recursively = settings.recursively
    default_tags = settings.tags

    def __init__(self, *,
                 names=None, tags=None,
                 file=None, basedir=None, recursively=None,
                 **find_params):
        if names is None:
            names = self.default_names
        if tags is None:
            tags = self.default_tags
        if file is None:
            file = self.default_file
        if basedir is None:
            basedir = self.default_basedir
        if recursively is None:
            recursively = self.default_recursively
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        self._find_params = find_params

    def __call__(self):
        Modules = self._find_objects(
            basedir=self._basedir,
            filename=self._filename,
            filepath=self._filepath,
            maxdepth=self._maxdepth,
            mappers=self._mappers,
            getfirst_exception=self._getfirst_exception,
            **self._find_params)
        return Modules

    # Protected

    _getfirst_exception = NotFound
    _find_objects = find_objects
    _Module = Module

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
    def _maxdepth(self):
        if not self._recursively:
            if self._filepath is None:
                return 1
        return None

    @cachedproperty
    def _mappers(self):
        mappers = []
        constraint = Constraint(
            self._Module, names=self._names, tags=self._tags)
        mappers.append(constraint)
        return mappers
