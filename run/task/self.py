class Metaclass(type):

    # Public

    def __getattr__(self, name):
        instance = self()
        instance = getattr(instance, name)
        return instance

    def __call__(self, name, *args, **kwargs):
        instance = self()
        instance = instance(*args, **kwargs)
        return instance


class self(metaclass=Metaclass):

    # Public

    def __init__(self):
        self.__get = False
        self.__name = ''
        self.__call = False
        self.__args = ()
        self.__kwargs = {}

    def __getattr__(self, name):
        name = '.'.join(filter(None, [self.__name, name]))
        self.__get = True
        self.__name = name
        return self

    def __call__(self, *args, **kwargs):
        self.__call = True
        self.__args = args
        self.__kwargs = kwargs
        return self

    def expand(self, module):
        result = module
        if self.__get:
            result = getattr(result, self.__name)
        if self.__call:
            result = result(*self.__args, **self.__kwargs)
        return result
