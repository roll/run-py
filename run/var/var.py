from abc import ABCMeta
from ..settings import settings
from ..task import Task


class Var(Task, metaclass=ABCMeta):

    # Public

    def __get__(self, module, module_class=None):
        if self.Cache:
            try:
                self.__cached_result
            except AttributeError:
                self.__cached_result = self()
            return self.__cached_result
        else:
            return self()

    @property
    def Cache(self):
        """Var's caching status (enabled or disabled).
        """
        return self.Inspect(
            'Cache', module=True, default=settings.cache)

    @property
    def Signature(self):
        return ''

    @property
    def Style(self):
        return self.Inspect('Style', default='var')
