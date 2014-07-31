from abc import ABCMeta, abstractmethod
from box.functools import Decorator

class Converter(Decorator, metaclass=ABCMeta):
    """Base abstract converter decorator.
    """

    # Public

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __call__(self, obj):
        result = obj
        if (not isinstance(obj, self._task_prototype_class) and
            not isinstance(obj, self._task_class)):
            result = self.invoke(obj)
        return result

    # Overriding
    def is_composite(self, *args, **kwargs):
        # Composite only if kwargs passed
        return not bool(args)

    @abstractmethod
    def invoke(self, obj):
        pass  # pragma: no cover

    # Protected

    _kwargs = {}
