from ..task import TaskPrototype, build

class ModulePrototype(TaskPrototype):

    # Public

    def __init__(self, cls, updates, *args, **kwargs):
        copied_class = cls.__copy__()
        super().__init__(copied_class, updates, *args, **kwargs)

    # Protected

    _task_prototype_class = TaskPrototype

    def _build_task(self, task, module):
        for name in dir(self._class):
            attr = getattr(self._class, name)
            if isinstance(attr, self._task_prototype_class):
                nested_task = build(attr, task)
                setattr(self._class, name, nested_task)
        super()._build_task(task, module)

    def _update_task(self, task):
        for nested_task in task.meta_tasks.values():
            nested_task.__update__()
        super()._update_task(task)
