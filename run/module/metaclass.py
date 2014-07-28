import inspect
from copy import copy
from ..attribute import AttributePrototype, AttributeMetaclass, Attribute
from ..task import Task, TaskPrototype, task
from ..var import var
from .prototype import ModulePrototype
from .skip import skip

class ModuleMetaclass(AttributeMetaclass):

    # Public

    def __new__(cls, name, bases, attrs):
        for key, attr in attrs.items():
            if key.isupper():
                continue
            if key.startswith('_'):
                continue
            if key.startswith('meta_'):
                continue
            if isinstance(attr, type):
                continue
            # TODO: remove
            if isinstance(attr, cls._attribute_class):
                continue
            # TODO: remove
            if isinstance(attr, cls._attribute_prototype_class):
                continue
            if isinstance(attr, cls._task_prototype_class):
                continue
            if isinstance(attr, cls._task_class):
                continue
            if isinstance(attr, staticmethod):
                continue
            if isinstance(attr, classmethod):
                continue
            if getattr(attr, '__isabstractmethod__', False):
                continue
            if getattr(attr, skip.attribute_name, False):
                continue
            if callable(attr):
                # Task
                attrs[key] = cls._task(attr)
            elif inspect.isdatadescriptor(attr):
                # Var
                attrs[key] = cls._var(attr)
        return super().__new__(cls, name, bases, attrs)

    def __copy__(self):
        attrs = {}
        for cls in self.mro():
            for key, attr in vars(cls).items():
                if (key not in attrs and
                    # TODO: remove attribute
                    (isinstance(attr, self._attribute_prototype_class) or
                     isinstance(attr, self._task_prototype_class))):
                    attrs[key] = copy(attr)
        attrs['__doc__'] = self.__doc__
        attrs['__module__'] = self.__module__
        return type(self)(self.__name__, (self,), attrs)

    # Protected

    _attribute_class = Attribute
    _attribute_prototype_class = AttributePrototype
    _prototype_class = ModulePrototype  # Overriding
    _task_prototype_class = TaskPrototype
    _task_class = Task
    _task = task
    _var = var
