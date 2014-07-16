import inspect

class CommonConstraint:

    # Public

    def __init__(self, module_class):
        self._module_class = module_class

    def __call__(self, emitter):
        if inspect.getmodule(emitter.object) != emitter.module:
            emitter.skip()
        elif not isinstance(emitter.object, type):
            emitter.skip()
        elif not issubclass(emitter.object, self._module_class):
            emitter.skip()
