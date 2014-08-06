from abc import ABCMeta
from box.types import Null
from ..settings import settings
from ..task import Task
from .signal import InitiatedVarSignal, SuccessedVarSignal, FailedVarSignal


class Var(Task, metaclass=ABCMeta):

    # Public

    def __initiate__(self, *args, **kwargs):
        self._meta_cached_value = Null
        return super().__initiate__(*args, **kwargs)

    def __get__(self, module, module_class=None):
        if self.meta_cache:
            if self._meta_cached_value is Null:
                self._meta_cached_value = self()
            return self._meta_cached_value
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

    _meta_color_code = settings.var_color_code
    _meta_FailedTaskSignal = FailedVarSignal  # Overriding
    _meta_InitiatedTaskSignal = InitiatedVarSignal  # Overriding
    _meta_SuccessedTaskSignal = SuccessedVarSignal  # Overriding
