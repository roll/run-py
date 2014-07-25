from abc import ABCMeta
from box.functools import Null
from box.importlib import inject
from .build import build
from .prototype import AttributePrototype

class AttributeMetaclass(ABCMeta):

    # Public

    def __call__(self, *args, **kwargs):
        module = kwargs.pop('meta_module', Null)
        prototype = self._prototype_class(self, None, *args, **kwargs)
        if module != Null:
            if module == None:
                module = self._null_module_class()
            return build(prototype, module)
        else:
            return prototype

    # Protected

    _null_module_class = inject('NullModule', module='run.module')
    _prototype_class = AttributePrototype
