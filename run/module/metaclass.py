import inspect
from copy import copy
from box.importlib import import_object
from ..settings import settings
from ..task import Task, TaskMetaclass, TaskPrototype
from .prototype import ModulePrototype
from .skip import skip

class ModuleMetaclass(TaskMetaclass):

    # Public

    def __new__(cls, name, bases, attrs):
        if cls._convert:
            for key, attr in attrs.items():
                if key.isupper():
                    continue
                if key.startswith('_'):
                    continue
                if key.startswith('meta_'):
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
                if isinstance(attr, type):
                    # Module
                    module = import_object(cls._module)
                    try:
                        attrs[key] = module(attr)
                    except TypeError:
                        pass
                elif callable(attr):
                    # Task
                    task = import_object(cls._task)
                    attrs[key] = task(attr)
                elif inspect.isdatadescriptor(attr):
                    # Var
                    var = import_object(cls._var)
                    attrs[key] = var(attr)
        return super().__new__(cls, name, bases, attrs)

    def __copy__(self):
        attrs = {}
        for cls in self.mro():
            for key, attr in vars(cls).items():
                if key not in attrs:
                    if isinstance(attr, self._task_prototype_class):
                        attrs[key] = copy(attr)
        attrs['__doc__'] = self.__doc__
        attrs['__module__'] = self.__module__
        return type(self)(self.__name__, (self,), attrs)

    # Protected

    _convert = settings.convert
    _module = settings.converters[0]
    _prototype_class = ModulePrototype  # Overriding
    _task_prototype_class = TaskPrototype
    _task_class = Task
    _task = settings.converters[1]
    _var = settings.converters[2]
