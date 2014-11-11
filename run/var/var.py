from abc import ABCMeta
from ..settings import settings
from ..task import Task


class Var(Task, metaclass=ABCMeta):

    # Public

    def __get__(self, module, module_class=None):
        if self.meta_cache:
            try:
                self.__cached_result
            except AttributeError:
                self.__cached_result = self()
            return self.__cached_result
        else:
            return self()

    @property
    def meta_cache(self):
        """Var's caching status (enabled or disabled).
        """
        return self.meta_retrieve(
            'cache', module=True, default=settings.cache)

    @property
    def meta_signature(self):
        return ''

    @property
    def meta_style(self):
        return self.meta_retrieve('style', default='var')
