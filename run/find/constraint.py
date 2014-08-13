import inspect
from box.find import Constraint


class Constraint(Constraint):

    # Public

    def __init__(self, target, *, names=None, tags=None):
        self._target = target
        self._names = names
        self._tags = tags

    def __call__(self, emitter):
        if inspect.getmodule(emitter.objself) != emitter.module:
            emitter.skip()
        elif not isinstance(emitter.objself, type):
            emitter.skip()
        elif not issubclass(emitter.objself, self._target):
            emitter.skip()
        elif not self._match_names(emitter.objself.meta_name):
            emitter.skip()
        elif not self._match_tags(emitter.objself.meta_tags):
            emitter.skip()

    # Protected

    def _match_names(self, name):
        if self._names is not None:
            if inspect.isdatadescriptor(name):
                return False
            elif name not in self._names:
                return False
        return True

    def _match_tags(self, tags):
        if self._tags is not None:
            if inspect.isdatadescriptor(tags):
                return False
            elif set(tags).isdisjoint(self._tags):
                return False
        return True
