from ..task import TaskPrototype, build

class ModulePrototype(TaskPrototype):

    # Public

    def __init__(self, *args, meta_class, **kwargs):
        eclass = meta_class.__copy__()
        super().__init__(*args, meta_class=eclass, **kwargs)

    # Protected

    _task_prototype_class = TaskPrototype

#     def _create_task(self):
#         class_copy = type(task).__copy__()
#         task = class_copy.__create__(self)
#         return task

    def _initiate_task(self, task, module):
        for name in dir(type(task)):
            attr = getattr(type(task), name)
            if isinstance(attr, self._task_prototype_class):
                nested_task = build(attr, task)
                setattr(type(task), name, nested_task)
        return super()._initiate_task(task, module)

    def _update_task(self, task):
        for name, nested_task in task.meta_tasks.items():
            nested_task = nested_task.__update__()
            setattr(type(task), name, nested_task)
        return super()._update_task(task)
