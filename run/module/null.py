import os
from box.functools import cachedproperty
from box.importlib import import_object
from ..settings import settings

class NullModule:

    # Public

    def __bool__(self):
        return False

    def __repr__(self):
        return '<NullModule>'

    @property
    def meta_basedir(self):
        return os.getcwd()

    @property
    def meta_cache(self):
        return self._meta_default_cache

    @property
    def meta_chdir(self):
        return self._meta_default_chdir

    @property
    def meta_color_name(self):
        return self._name

    @property
    def meta_color_qualname(self):
        return self._qualname

    @cachedproperty
    def meta_dispatcher(self):
        NullDispatcher = import_object(self._meta_null_dispatcher)
        dispatcher = NullDispatcher()
        return dispatcher

    @property
    def meta_docstring(self):
        return 'NullModule'

    @property
    def meta_fallback(self):
        return self._meta_default_fallback

    @property
    def meta_grayscale(self):
        return self._meta_default_grayscale

    @property
    def meta_is_main_module(self):
        return True

    @property
    def meta_main_module(self):
        return self

    @property
    def meta_module(self):
        return self

    @property
    def meta_name(self):
        return self._meta_default_main_module_name

    @property
    def meta_qualname(self):
        return self.meta_name

    @property
    def meta_strict(self):
        return self._meta_default_strict

    @property
    def meta_tags(self):
        return []

    @property
    def meta_type(self):
        return type(self).__name__

    @property
    def meta_tasks(self):
        return {}

    # Protected

    _meta_null_dispatcher = settings.null_dispatcher
    _meta_default_cache = settings.cache
    _meta_default_chdir = settings.chdir
    _meta_default_fallback = settings.fallback
    _meta_default_grayscale = settings.grayscale
    _meta_default_main_module_name = settings.main_module_name
    _meta_default_strict = settings.strict
