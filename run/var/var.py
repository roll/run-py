from abc import ABCMeta
from box.types import Null
from ..task import Task
from .signal import VarSignal


class Var(Task, metaclass=ABCMeta):

    # Public

    def __init__(self, *args, **kwargs):
        self._cached_value = Null
        super().__init__(*args, **kwargs)

    def __get__(self, module, module_class=None):
        if self.meta_cache:
            if self._cached_value is Null:
                self._cached_value = self()
            return self._cached_value
        else:
            return self()

    @property
    def meta_cache(self):
        """Var's caching status (enabled or disabled).

        If meta_cache is True var caches
        results after first invocation.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get(
            'cache', self.meta_module.meta_cache)

    @meta_cache.setter
    def meta_cache(self, value):
        self._meta_params['cache'] = value

    @property
    def meta_signature(self):
        return ''

    # Protected

    _meta_style = 'var'  # Overriding
    _meta_TaskSignal = VarSignal  # Overriding
