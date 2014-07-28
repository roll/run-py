import inspect
from copy import copy
from ..task import Task, TaskMetaclass, TaskPrototype, task
from ..var import var
from .prototype import ModulePrototype
from .skip import skip

class ModuleMetaclass(TaskMetaclass):

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
                    isinstance(attr, self._task_prototype_class)):
                    attrs[key] = copy(attr)
        attrs['__doc__'] = self.__doc__
        attrs['__module__'] = self.__module__
        return type(self)(self.__name__, (self,), attrs)

    # Protected

    _prototype_class = ModulePrototype  # Overriding
    _task_prototype_class = TaskPrototype
    _task_class = Task
    _task = task
    _var = var
