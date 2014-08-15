from ..task import TaskPrototype, build
from .spawn import spawn


class ModulePrototype(TaskPrototype):

    # Protected

    _meta_TaskPrototype = TaskPrototype

    def _meta_create_task(self, cls, parent_module):
        spawned_class = spawn(cls)
        module = super()._meta_create_task(spawned_class, parent_module)
        for name in dir(type(module)):
            attr = getattr(type(module), name)
            if isinstance(attr, self._meta_TaskPrototype):
                task = build(attr, module)
                setattr(type(module), name, task)
        return module

    def _meta_update_task(self, module):
        for task in module.meta_tasks.values():
            task.__meta_update__()
        super()._meta_update_task(module)
