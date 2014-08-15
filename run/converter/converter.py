from abc import ABCMeta, abstractmethod
from box.functools import Decorator
from .skip import skip


class Converter(Decorator, metaclass=ABCMeta):
    """Base abstract converter decorator.
    """

    # Public

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __call__(self, obj):
        if self.check_converted(obj):
            return obj
        if self.check_applicable(obj):
            if self.check_matched(obj):
                return self.make(obj)
        raise TypeError(
            'Converter "{self}" is not suitable converter '
            'for the given object "{obj}" convertation.'.
            format(self=self, obj=obj))

    def is_composite(self, *args, **kwargs):  # Overriding
        # Composite only if args not passed
        return not bool(args)

    def check_applicable(self, obj):
        if isinstance(obj, staticmethod):
            return False
        if isinstance(obj, classmethod):
            return False
        if getattr(obj, '__isabstractmethod__', False):
            return False
        if getattr(obj, skip.attribute_name, False):
            return False
        return True

    @abstractmethod
    def check_converted(self, obj):
        pass  # pragma: no cover

    @abstractmethod
    def check_matched(self, obj):
        pass  # pragma: no cover

    @abstractmethod
    def make(self, obj):
        pass  # pragma: no cover

    # Protected

    _kwargs = {}
