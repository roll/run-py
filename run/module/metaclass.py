from ..converter import convert
from ..settings import settings
from ..task import TaskMetaclass, TaskPrototype, fork
from .prototype import ModulePrototype

class ModuleMetaclass(TaskMetaclass):

    # Public

    def __copy__(self):
        attrs = {}
        for cls in self.mro():
            for key, attr in vars(cls).items():
                if key in attrs:
                    continue
                if key.isupper():
                    continue
                if key.startswith('_'):
                    continue
                if key.startswith('meta_'):
                    continue
                if isinstance(attr, self._task_prototype_class):
                    attrs[key] = fork(attr)
                else:
                    if self._default_convert:
                        try:
                            attrs[key] = convert(attr)
                        except TypeError:
                            pass
        attrs['__doc__'] = self.__doc__
        attrs['__module__'] = self.__module__
        return type(self)(self.__name__, (self,), attrs)

    # Protected

    _default_convert = settings.convert
    _prototype_class = ModulePrototype  # Overriding
    _task_prototype_class = TaskPrototype
