from abc import ABCMeta, abstractmethod
from box.functools import Decorator
from .result import Result
from .skip import skip


class Converter(Decorator, metaclass=ABCMeta):
    """Base abstract converter decorator.
    """

    # Public

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __call__(self, obj):
        if self._check_converted(obj):
            return obj
        if self._check_eligible(obj):
            if self._match(obj):
                return self._make(obj)
        raise TypeError(
            'Converter "{self}" is not suitable converter '
            'for the given object "{obj}" convertation.'.
            format(self=self, obj=obj))

    # Protected

    _kwargs = {}

    def _is_composite(self, *args, **kwargs):  # Overriding
        # Composite only if args not passed
        return not bool(args)

    def _check_converted(self, obj):
        return isinstance(obj, Result)

    def _check_eligible(self, obj):
        if isinstance(obj, staticmethod):
            return False
        if isinstance(obj, classmethod):
            return False
        if getattr(obj, skip.attribute_name, False):
            return False
        return True

    @abstractmethod
    def _match(self, obj):
        pass  # pragma: no cover

    @abstractmethod
    def _make(self, obj):
        pass  # pragma: no cover
