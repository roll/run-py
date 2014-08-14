from ..converter import convert
from ..task import TaskMetaclass, TaskPrototype, fork
from .prototype import ModulePrototype


class ModuleMetaclass(TaskMetaclass):

    # Public

    def __spawn__(self):
        # Documented public wrapper in :func:`.spawn`
        keys = []
        attrs = {}
        for cls in self.mro():
            for key, attr in vars(cls).items():
                if key in keys:
                    continue
                keys.append(key)
                if key.isupper():
                    continue
                elif key.startswith('_'):
                    continue
                elif key.startswith('meta_'):
                    continue
                elif isinstance(attr, self._BaseTaskPrototype):
                    attrs[key] = self._fork(attr)
                else:
                    if cls.meta_convert:
                        try:
                            attrs[key] = self._convert(attr)
                        except TypeError:
                            pass
        attrs['__doc__'] = self.__doc__
        attrs['__module__'] = self.__module__
        return type(self)(self.__name__, (self,), attrs)

    # Protected

    _BaseTaskPrototype = TaskPrototype
    _convert = convert
    _fork = staticmethod(fork)
    _TaskPrototype = ModulePrototype  # Overriding
