from abc import ABCMeta
from .prototype import Prototype


class Metaclass(ABCMeta):

    # Public

    def __call__(self, *args,
                 Build=False, Module=None, Updates=None, **kwargs):
        result = Prototype(*args, Class=self, Updates=Updates, **kwargs)
        if Build:
            result = result.Build(Module=Module)
        return result
