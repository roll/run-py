from abc import ABCMeta
from .prototype import Prototype


class Metaclass(ABCMeta):

    # Public

    def __call__(self, *args, meta_build=False,
                 meta_module=None, meta_updates=None, **kwargs):
        result = Prototype(
            *args, meta_class=self, meta_updates=meta_updates, **kwargs)
        if meta_build:
            result = result.meta_build(meta_module=meta_module)
        return result
