import os
from box.find import find_objects
from box.functools import Function, cachedproperty
from ..settings import settings
from .constraint import Constraint
from .not_found import NotFound
from .target import Target


class find(Function):
    """Find run modules.
    """

    # Public

    default_basedir = settings.basedir
    default_file = settings.file
    default_key = settings.key
    default_recursively = settings.recursively
    default_tags = settings.tags
    default_target = Target

    def __init__(self, *,
                 target=None,
                 key=None, tags=None,
                 file=None, basedir=None, recursively=None,
                 **find_params):
        if target is None:
            target = self.default_target
        if key is None:
            key = self.default_key
        if tags is None:
            tags = self.default_tags
        if file is None:
            file = self.default_file
        if basedir is None:
            basedir = self.default_basedir
        if recursively is None:
            recursively = self.default_recursively
        self._target = target
        self._key = key
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        self._find_params = find_params

    def __call__(self):
        result = self._find_objects(
            basedir=self._basedir,
            filepathes=self._filepathes,
            filters=self._effective_filters,
            constraints=self._effective_constraints,
            getfirst_exception=self._getfirst_exception,
            **self._find_params)
        return result

    # Protected

    _find_objects = find_objects
    _getfirst_exception = NotFound

    @property
    def _effective_filters(self):
        filters = []
        if self._filepathes is None:
            filters.append({'filename': self._file})
            if not self._recursively:
                filters.append({'maxdepth': 1})
        filters += self._find_params.pop('filters', [])
        return filters

    @cachedproperty
    def _effective_constraints(self):
        constraints = [
            Constraint(self._target, key=self._key, tags=self._tags)]
        constraints += self._find_params.pop('constraints', [])
        return constraints

    @property
    def _filepathes(self):
        if self._file is not None:
            if os.path.sep in self._file:
                return [self._file]
        return None
