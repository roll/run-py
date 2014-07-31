from box.functools import Function
from box.importlib import import_object
from ..settings import settings

class convert(Function):
    """Convert object using converters from settings.
    """

    # Public

    def __init__(self, obj):
        self._object = obj

    def __call__(self):
        for converter in self._converters:
            converter = import_object(converter)
            try:
                return converter(self._object)
            except TypeError:
                pass
        raise TypeError(
            'Object "{self._object}" has no corresponding converter '
            'between converters from settings: {self._converters}'.
            format(self=self))

    # Protected

    _converters = settings.converters
