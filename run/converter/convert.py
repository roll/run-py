from box.functools import Function
from box.importlib import import_object
from ..settings import settings


class convert(Function):
    """Convert object using converters from settings.
    """

    # Public

    def __init__(self, obj):
        self.__object = obj

    def __call__(self):
        for converter in settings.converters:
            converter = import_object(converter)
            try:
                return converter(self.__object)
            except TypeError:
                pass
        raise TypeError(
            'Object "{object}" has no corresponding converter '
            'between converters from settings: {converters}'.
            format(object=self.__object,
                   converters=settings.converters))
