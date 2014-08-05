from abc import ABCMeta
from box.importlib import import_object
from box.types import Null
from ..settings import settings
from .build import build
from .prototype import TaskPrototype

class TaskMetaclass(ABCMeta):

    # Public

    def __call__(self, *args, **kwargs):
        module = kwargs.pop('meta_module', Null)
        prototype = self._prototype_class(*args, meta_class=self, **kwargs)
        if module is not Null:
            if module is None:
                NullModule = import_object(self._null_module)
                module = NullModule()
            return build(prototype, module)
        else:
            return prototype

    # Protected

    # TODO: renamed to _meta (if accessable from Task class)?
    _null_module = settings.null_module
    _prototype_class = TaskPrototype
