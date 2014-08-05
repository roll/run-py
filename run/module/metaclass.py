from ..converter import convert
from ..settings import settings
from ..task import TaskMetaclass, TaskPrototype, fork
from .prototype import ModulePrototype

class ModuleMetaclass(TaskMetaclass):

    # Public

    def __spawn__(self):
        keys = []
        attrs = {}
        for cls in self.mro():
            for key, attr in vars(cls).items():
                if key in keys:
                    continue
                keys.append(key)
                if key.isupper():
                    continue
                if key.startswith('_'):
                    continue
                if key.startswith('meta_'):
                    continue
                if isinstance(attr, self._task_prototype_class):
                    attrs[key] = self._fork(attr)
                else:
                    if self._default_convert:
                        try:
                            attrs[key] = self._convert(attr)
                        except TypeError:
                            pass
        attrs['__doc__'] = self.__doc__
        attrs['__module__'] = self.__module__
        return type(self)(self.__name__, (self,), attrs)

    # Protected

    _convert = convert
    _default_convert = settings.convert
    _fork = staticmethod(fork)
    _prototype_class = ModulePrototype  # Overriding
    _task_prototype_class = TaskPrototype
