import inspect
from box.find import Constraint


class Constraint(Constraint):

    # Public

    def __init__(self, target, *, key=None, tags=None):
        self._target = target
        self._key = key
        self._tags = tags

    def __call__(self, emitter):
        if inspect.getmodule(emitter.objself) != emitter.module:
            emitter.skip()
        elif not isinstance(emitter.objself, type):
            emitter.skip()
        elif not issubclass(emitter.objself, self._target):
            emitter.skip()
        elif not self._match_key(emitter.objself.meta_key):
            emitter.skip()
        elif not self._match_tags(emitter.objself.meta_tags):
            emitter.skip()

    # Protected

    def _match_key(self, key):
        if self._key is not None:
            if key != self._key:
                return False
        return True

    def _match_tags(self, tags):
        if self._tags is not None:
            if set(tags).isdisjoint(self._tags):
                return False
        return True
