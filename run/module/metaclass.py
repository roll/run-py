from ..converter import convert
from ..task import TaskMetaclass, TaskPrototype, fork
from .prototype import ModulePrototype


class ModuleMetaclass(TaskMetaclass):

    # Public

    def __meta_spawn__(self):
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
                elif isinstance(attr, self._meta_BaseTaskPrototype):
                    attrs[key] = self._meta_fork(attr)
                else:
                    if cls.meta_convert:
                        try:
                            attrs[key] = self._meta_convert(attr)
                        except TypeError:
                            pass
        attrs['__doc__'] = self.__doc__
        attrs['__module__'] = self.__module__
        return type(self)(self.__name__, (self,), attrs)

    # Protected

    _meta_BaseTaskPrototype = TaskPrototype
    _meta_convert = convert
    _meta_fork = staticmethod(fork)
    _meta_TaskPrototype = ModulePrototype  # Overriding
