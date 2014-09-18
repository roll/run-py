from abc import ABCMeta
from box.types import Null
from .build import build
from .prototype import Prototype


class Metaclass(ABCMeta):

    # Public

    def __call__(self, *args, meta_module=Null, meta_updates=None, **kwargs):
        prototype = Prototype(
            *args, meta_class=self, meta_updates=meta_updates, **kwargs)
        if meta_module is Null:
            # Return prototype
            return prototype
        else:
            # Build and return task
            task = build(prototype, meta_module)
            return task
