import os
from box.functools import cachedproperty
from ..signal import NullDispatcher
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

    @cachedproperty
    def meta_dispatcher(self):
        return self._meta_dispatcher_class()

    @property
    def meta_docstring(self):
        return 'NullModule'

    @property
    def meta_fallback(self):
        return self._meta_default_fallback

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

    _meta_dispatcher_class = NullDispatcher
    _meta_default_cache = settings.default_cache
    _meta_default_chdir = settings.default_chdir
    _meta_default_fallback = settings.default_fallback
    _meta_default_main_module_name = settings.default_meta_main_module_name
    _meta_default_strict = settings.default_meta_strict
