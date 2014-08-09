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

    def __init__(self, *filters,
                 names=None, tags=None,
                 file=None, basedir=None, recursively=None,
                 **params):
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
        self._filters = filters
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        self._params = params

    def __call__(self):
        Modules = self._find_objects(
            *self._effective_filters,
            basedir=self._basedir,
            filepathes=self._filepathes,
            mappers=self._effective_mappers,
            getfirst_exception=self._NotFound,
            **self._params)
        return Modules

    # Protected

    _find_objects = find_objects
    _Module = Module
    _NotFound = NotFound

    @property
    def _effective_filters(self):
        filters = []
        if self._filepathesis is not None:
            filters.append({'filename': self._file})
            if not self._recursively:
                filters.append({'maxdepth': 1})
        filters += self._filters
        return filters

    @property
    def _filepathes(self):
        if self._file is not None:
            if os.path.sep in self._file:
                return [self._file]
        return None

    @cachedproperty
    def _effective_mappers(self):
        mappers = []
        constraint = Constraint(
            self._Module, names=self._names, tags=self._tags)
        mappers.append(constraint)
        mappers += self.params.pop('mappers', [])
        return mappers
