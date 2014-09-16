from ..task import TaskPrototype, build
from .spawn import spawn


class ModulePrototype(TaskPrototype):

    # Protected

    def __meta_create__(self, cls, parent_module):
        names = []
        spawned_class = spawn(cls)
        module = super().__meta_create__(spawned_class, parent_module)
        for cls in type(module).mro():
            for name, attr in vars(cls).items():
                if name in names:
                    continue
                names.append(name)
                if isinstance(attr, TaskPrototype):
                    task = build(attr, module)
                    setattr(type(module), name, task)
        return module

    def __meta_update__(self, module):
        for task in module.meta_tasks.values():
            task.__meta_update__()
        super().__meta_update__(module)
