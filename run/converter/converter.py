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
        if self.match(obj):
            return self.make(obj)
        else:
            raise TypeError(
                'Converter "{self}" can not convert object "{obj}"'.
                format(self=self, obj=obj))

    def match(self, obj):
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
    def make(self, obj):
        pass  # pragma: no cover

    def is_composite(self, *args, **kwargs):  # Overriding
        # Composite only if args not passed
        return not bool(args)

    # Protected

    _kwargs = {}
