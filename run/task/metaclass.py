from abc import ABCMeta
from box.importlib import import_object
from box.types import Null
from ..settings import settings
from .build import build
from .prototype import TaskPrototype


class TaskMetaclass(ABCMeta):

    # Public

    def __call__(self, *args, meta_module=Null, meta_updates=None, **kwargs):
        prototype = self._TaskPrototype(
            *args, meta_class=self, meta_updates=meta_updates, **kwargs)
        if meta_module is Null:
            # Return prototype
            return prototype
        else:
            # Build and return task
            if meta_module is None:
                NullModule = import_object(self._null_module)
                meta_module = NullModule()
            task = build(prototype, meta_module)
            return task

    # Protected

    # TODO: renamed to _meta (if accessable from Task class)?
    _null_module = settings.null_module
    _TaskPrototype = TaskPrototype
