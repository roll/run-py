from sugarbowl import Function, import_object
from ..settings import settings
from .exception import ConvertError


class convert(Function):
    """Convert object using converters from settings.
    """

    # Public

    def __init__(self, obj, **kwargs):
        self.__object = obj
        self.__kwargs = kwargs

    def __call__(self):
        for converter in settings.converters:
            converter = import_object(converter)
            try:
                if self.__kwargs:
                    converter = converter(**self.__kwargs)
                converted_object = converter(self.__object)
                return converted_object
            except ConvertError:
                pass
        raise ConvertError(
            'Object "{object}" has no corresponding converter '
            'between converters from settings: {converters}'.
            format(object=self.__object,
                   converters=settings.converters))
