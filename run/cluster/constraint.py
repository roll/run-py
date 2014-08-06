import inspect

class Constraint:

    # Public

    def __init__(self, module, *, names=None, tags=None):
        self._Module = module
        self._names = names
        self._tags = tags

    def __call__(self, emitter):
        if inspect.getmodule(emitter.object) != emitter.module:
            emitter.skip()
        elif not isinstance(emitter.object, type):
            emitter.skip()
        elif not issubclass(emitter.object, self._Module):
            emitter.skip()
        elif not self._match_names(emitter.object.meta_name):
            emitter.skip()
        elif not self._match_tags(emitter.object.meta_tags):
            emitter.skip()

    # Protected

    def _match_names(self, name):
        if self._names:
            if inspect.isdatadescriptor(name):
                return False
            elif name not in self._names:
                return False
        return True

    def _match_tags(self, tags):
        if self._tags:
            if inspect.isdatadescriptor(tags):
                return False
            elif set(tags).isdisjoint(self._tags):
                return False
        return True
