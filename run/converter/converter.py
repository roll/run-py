from abc import ABCMeta, abstractmethod
from box.functools import Decorator
from .converted import Converted
from .skip import skip


class Converter(Decorator, metaclass=ABCMeta):
    """Base abstract converter decorator.
    """

    # Public

    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def __call__(self, obj):
        if self.__check_converted(obj):
            return obj
        if self.__check_eligible(obj):
            if self._match(obj):
                return self._make(obj)
        raise TypeError(
            'Converter "{self}" is not suitable converter '
            'for the given object "{obj}" convertation.'.
            format(self=self, obj=obj))

    # TODO: improve implementation?
    def is_composite(self, *args, **kwargs):
        if not super().is_composite(*args, **kwargs):
            return False
        try:
            return not isinstance(args[0], Converted)
        except IndexError:
            return True

    # Protected

    @abstractmethod
    def _match(self, obj):
        pass  # pragma: no cover

    @abstractmethod
    def _make(self, obj):
        pass  # pragma: no cover

    @property
    def _kwargs(self):
        return self.__kwargs

    # Private

    def __check_converted(self, obj):
        return isinstance(obj, Converted)

    def __check_eligible(self, obj):
        if isinstance(obj, staticmethod):
            return False
        if isinstance(obj, classmethod):
            return False
        if getattr(obj, skip.attribute_name, False):
            return False
        return True
