from ..task import TaskPrototype, build

class ModulePrototype(TaskPrototype):

    # Public

    def __init__(self, *args, meta_class, **kwargs):
        eclass = meta_class.__copy__()
        super().__init__(*args, meta_class=eclass, **kwargs)

    # Protected

    _task_prototype_class = TaskPrototype

    def _build_task(self, task, module):
        for name in dir(self._class):
            attr = getattr(self._class, name)
            if isinstance(attr, self._task_prototype_class):
                nested_task = build(attr, task)
                setattr(self._class, name, nested_task)
        return super()._build_task(task, module)

    def _update_task(self, task):
        for nested_task in task.meta_tasks.values():
            nested_task.__update__()
        super()._update_task(task)
