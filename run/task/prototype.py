from copy import copy
from .update import TaskUpdate


class TaskPrototype:

    # Public

    def __init__(self, *args, meta_class, meta_updates=None, **kwargs):
        if meta_updates is None:
            meta_updates = []
        super().__setattr__('_class', meta_class)
        super().__setattr__('_updates', meta_updates)
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)

    def __meta_fork__(self, *args, **kwargs):
        # Documented public wrapper in :func:`.fork`
        eupdates = copy(self._updates)
        eargs = self._args + args
        ekwargs = self._kwargs
        ekwargs.update(kwargs)
        return type(self)(
            *eargs,
            meta_class=self._class,
            meta_updates=eupdates,
            **ekwargs)

    def __meta_build__(self, module):
        # Documented public wrapper in :func:`.build`
        task = self._create_task(self._class, module)
        if not module:
            # NullModule
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
        self._add_update('meta_disable_dependency', *args, **kwargs)

    def meta_enable_dependency(self, *args, **kwargs):
        self._add_update('meta_enable_dependency', *args, **kwargs)

    def meta_require(self, *args, **kwargs):
        self._add_update('meta_require', *args, **kwargs)

    def meta_trigger(self, *args, **kwargs):
        self._add_update('meta_trigger', *args, **kwargs)

    # Protected

    _TaskUpdate = TaskUpdate

    def _add_update(self, name, *args, **kwargs):
        update = self._TaskUpdate(name, *args, **kwargs)
        self._updates.append(update)

    def _create_task(self, cls, module):
        task = cls.__meta_create__(
            *self._args,
            meta_module=module,
            meta_updates=self._updates,
            **self._kwargs)
        return task

    def _update_task(self, task):
        task.__meta_update__()
