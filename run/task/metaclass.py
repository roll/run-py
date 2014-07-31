from abc import ABCMeta
from box.importlib import inject
from box.types import Null
from .build import build
from .prototype import TaskPrototype

class TaskMetaclass(ABCMeta):

    # Public

    def __call__(self, *args, **kwargs):
        module = kwargs.pop('meta_module', Null)
        prototype = self._prototype_class(self, None, *args, **kwargs)
        if module is not Null:
            if module is None:
                module = self._null_module_class()
            return build(prototype, module)
        else:
            return prototype

    # Protected

    # TODO: remove module dependency, may be using settings IoC?
    _null_module_class = inject('NullModule', module='run.module')
    _prototype_class = TaskPrototype
