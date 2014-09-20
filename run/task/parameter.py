import inspect
from box.types import Null; Null  # PyDev warning bug


class Parameter:

    # Public

    def __init__(self, name, *,
                 writable=False, inheritable=False,
                 default=Null, docstring=None):
        self.__name = name
        self.__writable = writable
        self.__inheritable = inheritable
        self.__default = default
        self.__doc__ = docstring

    def __get__(self, objself, objtype):
        default = self.__default
        if inspect.isfunction(self.__default):
            default = self.__default(objself)
        return objself._meta_get_parameter(
            self.__name, inherit=self.__inheritable, default=default)

    def __set__(self, objself, value):
        if not self.__writable:
            raise AttributeError('can\'t set attribute')
        objself._meta_set_parameter(self.__name, value)

    def default(self, function):
        self.__default = function

