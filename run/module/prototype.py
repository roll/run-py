from ..task import TaskPrototype, build

class ModulePrototype(TaskPrototype):

    # Public

    def __init__(self, cls, updates, *args, **kwargs):
        copied_class = cls.__copy__()
        super().__init__(copied_class, updates, *args, **kwargs)

    # Protected

    _task_prototype_class = TaskPrototype

    def _create_task(self):
        module = super()._create_task()
        for name in dir(self._class):
            attr = getattr(self._class, name)
            if isinstance(attr, self._task_prototype_class):
                setattr(self._class, name, build(attr, module))
        return module
