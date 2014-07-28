from copy import copy
from .update import TaskUpdate

class TaskPrototype:

    # Public

    def __init__(self, cls, updates, *args, **kwargs):
        if updates is None:
            updates = []
        super().__setattr__('_class', cls)
        super().__setattr__('_updates', updates)
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)

    def __copy__(self, *args, **kwargs):
        # Documented public wrapper in :func:`.fork`
        eupdates = copy(self._updates)
        eargs = self._args + args
        ekwargs = self._kwargs
        ekwargs.update(kwargs)
        return type(self)(self._class, eupdates, *eargs, **ekwargs)

    def __build__(self, module):
        # Documented public wrapper in :func:`.build`
        task = self._create_task()
        self._init_task(task, module)
        self._update_task(task)
        return task

    def __getattr__(self, name):
        try:
            return getattr(self._class, name)
        except AttributeError:
            raise AttributeError(
                'Prototype {self} has no attribute {name}'.
                format(self=self, name=name)) from None

    def __setattr__(self, *args, **kwargs):
        self._add_update('__setattr__', *args, **kwargs)

    def meta_depend(self, *args, **kwargs):
        self._add_update('meta_depend', *args, **kwargs)

    def meta_disable_dependency(self, *args, **kwargs):
        self._add_update('disable_dependency', *args, **kwargs)

    def meta_enable_dependency(self, *args, **kwargs):
        self._add_update('enable_dependency', *args, **kwargs)

    def meta_require(self, *args, **kwargs):
        self._add_update('meta_require', *args, **kwargs)

    def meta_trigger(self, *args, **kwargs):
        self._add_update('meta_trigger', *args, **kwargs)

    # Protected

    _update_class = TaskUpdate

    def _add_update(self, name, *args, **kwargs):
        self._updates.append(self._update_class(name, *args, **kwargs))

    def _create_task(self):
        return object.__new__(self._class)

    def _init_task(self, task, module):
        task.__build__(module, *self._args, **self._kwargs)

    def _update_task(self, task):
        for update in self._updates:
            update.apply(task)
