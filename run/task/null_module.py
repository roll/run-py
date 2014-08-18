import os
from box.functools import cachedproperty
from ..settings import settings
from ..signal import NullDispatcher
from .module import Module


class NullModule(Module):

    # Public

    def __bool__(self):
        return False

    def __repr__(self):
        return '<NullModule>'

    def meta_lookup(self, name):
        raise KeyError(name)

    @property
    def meta_basedir(self):
        return os.path.abspath(os.getcwd())

    @property
    def meta_cache(self):
        return self._meta_default_cache

    @property
    def meta_chdir(self):
        return self._meta_default_chdir

    @cachedproperty
    def meta_dispatcher(self):
        return self._meta_NullDispatcher()

    @property
    def meta_fallback(self):
        return self._meta_default_fallback

    @property
    def meta_fullname(self):
        return ''

    @property
    def meta_is_main_module(self):
        return True

    @property
    def meta_qualname(self):
        return ''

    @property
    def meta_main_module(self):
        return self

    @property
    def meta_plain(self):
        return self._meta_default_plain

    @property
    def meta_module(self):
        return self

    @property
    def meta_strict(self):
        return self._meta_default_strict

    @property
    def meta_tasks(self):
        return {}

    # Protected

    _meta_NullDispatcher = NullDispatcher
    _meta_default_cache = settings.cache
    _meta_default_chdir = settings.chdir
    _meta_default_fallback = settings.fallback
    _meta_default_plain = settings.plain
    _meta_default_strict = settings.strict
