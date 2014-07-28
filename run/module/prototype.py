from copy import copy
from ..task import TaskPrototype, build

class ModulePrototype(TaskPrototype):

    # Public

    def __init__(self, cls, updates, *args, **kwargs):
        eclass = copy(cls)
        super().__init__(eclass, updates, *args, **kwargs)

    # Protected

    _task_prototype_class = TaskPrototype

    def _create_attribute(self):
        module = super()._create_attribute()
        for name in dir(self._class):
            attr = getattr(self._class, name)
            if isinstance(attr, self._task_prototype_class):
                setattr(self._class, name, build(attr, module))
        return module
