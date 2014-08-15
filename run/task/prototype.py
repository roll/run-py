from copy import copy
from box.collections import merge_dicts
from .update import TaskUpdate


class TaskPrototype:

    # Public

    def __init__(self, *args, meta_class, meta_updates=None, **kwargs):
        if meta_updates is None:
            meta_updates = []
        self._meta_class = meta_class
        self._meta_updates = meta_updates
        self._meta_args = args
        self._meta_kwargs = kwargs

    def __meta_fork__(self, *args, **kwargs):
        # Documented public wrapper in :func:`.fork`
        eupdates = copy(self._meta_updates)
        eargs = self._meta_args + args
        ekwargs = merge_dicts(self._meta_kwargs, kwargs)
        return type(self)(
            *eargs,
            meta_class=self._meta_class,
            meta_updates=eupdates,
            **ekwargs)

    def __meta_build__(self, module):
        # Documented public wrapper in :func:`.build`
        task = self._meta_create_task(self._meta_class, module)
        if not module:
            # NullModule - update
            self._meta_update_task(task)
        return task

    def __getattr__(self, name):
        if name.startswith('_meta'):
            return super().__getattribute__(name)
        try:
            return getattr(self._meta_class, name)
        except AttributeError:
            raise AttributeError(
                'Prototype {self} has no attribute {name}'.
                format(self=self, name=name)) from None

    def __setattr__(self, name, value):
        if name.startswith('_meta'):
            return super().__setattr__(name, value)
        self._meta_add_update('__setattr__', name, value)

    def meta_depend(self, *args, **kwargs):
        self._meta_add_update('meta_depend', *args, **kwargs)

    def meta_disable_dependency(self, *args, **kwargs):
        self._meta_add_update('meta_disable_dependency', *args, **kwargs)

    def meta_enable_dependency(self, *args, **kwargs):
        self._meta_add_update('meta_enable_dependency', *args, **kwargs)

    def meta_require(self, *args, **kwargs):
        self._meta_add_update('meta_require', *args, **kwargs)

    def meta_trigger(self, *args, **kwargs):
        self._meta_add_update('meta_trigger', *args, **kwargs)

    # Protected

    _meta_TaskUpdate = TaskUpdate

    def _meta_add_update(self, name, *args, **kwargs):
        update = self._meta_TaskUpdate(name, *args, **kwargs)
        self._meta_updates.append(update)

    def _meta_create_task(self, cls, module):
        task = cls.__meta_create__(
            *self._meta_args,
            meta_module=module,
            meta_updates=self._meta_updates,
            **self._meta_kwargs)
        return task

    def _meta_update_task(self, task):
        task.__meta_update__()
