import inspect
from find import find_objects
from box.functools import Function
from ...module import Module
from ...settings import settings


class find_modules(Function):
    """Find run modules.
    """

    # Public

    default_filename = settings.filename

    def __init__(self, *, filename=None, key=None, tags=None,
                 filters=None, mappers=None, **params):
        if filename is None:
            filename = self.default_filename
        if filters is None:
            filters = []
        if mappers is None:
            mappers = []
        self.__filename = filename
        self.__key = key
        self.__tags = tags
        self.__filters = filters
        self.__mappers = mappers
        self.__params = params

    def __call__(self):
        filters = [self.__filter] + self.__filters
        mappers = [self.__mapper] + self.__mappers
        result = find_objects(
            filters=filters,
            mappers=mappers,
            **self.__params)
        return result

    # Private

    @property
    def __filter(self):
        return {'filename': self.__filename}

    def __mapper(self, emitter):
        if inspect.getmodule(emitter.objself) != emitter.module:
            emitter.skip()
        elif not isinstance(emitter.objself, type):
            emitter.skip()
        elif not issubclass(emitter.objself, Module):
            emitter.skip()
        elif not self.__match_key(emitter.objself.meta_key):
            emitter.skip()
        elif not self.__match_tags(emitter.objself.meta_tags):
            emitter.skip()

    def __match_key(self, key):
        if self.__key is not None:
            if key != self.__key:
                return False
        return True

    def __match_tags(self, tags):
        if self.__tags is not None:
            if set(tags).isdisjoint(self.__tags):
                return False
        return True
