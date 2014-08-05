from ..task import TaskPrototype, build

class ModulePrototype(TaskPrototype):

    # Public

    def __init__(self, *args, meta_class, **kwargs):
        eclass = meta_class.__copy__()
        super().__init__(*args, meta_class=eclass, **kwargs)

    # Protected

    _task_prototype_class = TaskPrototype

    # TODO: use self._class or type(task)?
    def _initiate_task(self, task, module):
        for name in dir(self._class):
            attr = getattr(self._class, name)
            if isinstance(attr, self._task_prototype_class):
                nested_task = build(attr, task)
                setattr(self._class, name, nested_task)
        return super()._initiate_task(task, module)

    # TODO: use self._class or type(task)?
    def _update_task(self, task):
        for name, nested_task in task.meta_tasks.items():
            nested_task = nested_task.__update__()
            setattr(self._class, name, nested_task)
        return super()._update_task(task)
