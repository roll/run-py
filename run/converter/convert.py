from box.functools import Function
from box.importlib import import_object
from ..settings import settings

class convert(Function):
    """Convert object using converters from settings.
    """

    # Public

    def __init__(self, obj):
        self._object = object

    def __call__(self):
        result = None
        for converter in self._converters:
            converter = import_object(converter)
            try:
                result = converter(self._object)
            except TypeError:
                pass
        if result is None:
            raise TypeError(
                'Object "{self._object}" has no corresponding converter'
                'between converters from settings: {self._converters}'.
                format(self=self))
        return result

    # Protected

    _converters = settings.converters
