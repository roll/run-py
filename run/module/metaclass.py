from ..converter import convert
from ..task import TaskMetaclass, TaskPrototype, fork
from .prototype import ModulePrototype


class ModuleMetaclass(TaskMetaclass):

    # Public

    def __meta_spawn__(self):
        # Documented public wrapper in :func:`.spawn`
        names = []
        attrs = {}
        for cls in self.mro():
            for name, attr in vars(cls).items():
                if name in names:
                    continue
                names.append(name)
                if name.isupper():
                    continue
                elif name.startswith('_'):
                    continue
                elif name.startswith('meta_'):
                    continue
                elif isinstance(attr, TaskPrototype):
                    attrs[name] = fork(attr)
                else:
                    if cls.meta_convert:
                        try:
                            attrs[name] = convert(attr)
                        except TypeError:
                            pass
        attrs['__doc__'] = self.__doc__
        attrs['__module__'] = self.__module__
        return type(self)(self.__name__, (self,), attrs)

    # Protected

    _meta_TaskPrototype = ModulePrototype  # override
