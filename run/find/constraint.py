import inspect
from find.frame import Constraint


class Constraint(Constraint):

    # Public

    def __init__(self, target, *, key=None, tags=None):
        self.__target = target
        self.__key = key
        self.__tags = tags

    def __call__(self, emitter):
        if inspect.getmodule(emitter.objself) != emitter.module:
            emitter.skip()
        elif not isinstance(emitter.objself, type):
            emitter.skip()
        elif not issubclass(emitter.objself, self.__target):
            emitter.skip()
        elif not self.__match_key(emitter.objself.meta_key):
            emitter.skip()
        elif not self.__match_tags(emitter.objself.meta_tags):
            emitter.skip()

    # Private

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
