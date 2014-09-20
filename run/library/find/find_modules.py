import os
from find import find_objects
from box.functools import Function, cachedproperty
from ...settings import settings
from .constraint import Constraint
from .not_found import NotFound


class find_modules(Function):
    """Find run modules.
    """

    # Public

    default_basedir = None
    default_exclude = None
    default_file = 'runfile.py'
    default_key = None
    default_recursively = False
    default_tags = None

    def __init__(self, *,
                 target=None,
                 key=None, tags=None,
                 file=None, exclude=None, basedir=None, recursively=None,
                 **find_params):
        if key is None:
            key = self.default_key
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
        self._key = key
        self._tags = tags
        self._file = file
        self._exclude = exclude
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
    def _filepathes(self):
        if self._file is not None:
            if os.path.sep in self._file:
                return [self._file]
        return None

    @property
    def _effective_filters(self):
        filters = []
        if self._filepathes is None:
            filters.append({'filename': self._file})
            if not self._recursively:
                filters.append({'maxdepth': 1})
        if self._exclude is not None:
            if os.path.sep not in self._exclude:
                filters.append({'notfilename': self._exclude})
            else:
                filters.append({'notfilepath': self._exclude})
        filters += self._find_params.pop('filters', [])
        return filters

    @cachedproperty
    def _effective_constraints(self):
        constraints = [
            Constraint(key=self._key, tags=self._tags)]
        constraints += self._find_params.pop('constraints', [])
        return constraints
