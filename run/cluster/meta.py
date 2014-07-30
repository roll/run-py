import inspect

class MetaConstraint:

    # Public

    def __init__(self, names, tags):
        self._names = names
        self._tags = tags

    def __call__(self, emitter):
        if self._names:
            if inspect.isdatadescriptor(emitter.object.meta_name):
                emitter.skip()
            elif emitter.object.meta_name not in self._names:
                emitter.skip()
        if self._tags:
            if inspect.isdatadescriptor(emitter.object.meta_tags):
                emitter.skip()
            elif set(emitter.object.meta_tags).isdisjoint(self._tags):
                emitter.skip()
