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
        self._meta_name = None

    def __getattr__(self, name):
        if name == '__isabstractmethod__':
            return super().__getattribute__(name)
        if hasattr(self._meta_class, name):
            attr = getattr(self._meta_class, name)
            # TODO: more attributes to forward from class?
            if isinstance(attr, type):
                return attr
        self._meta_name = self._meta_join_names(self._meta_name, name)
        return self

    def __setattr__(self, name, value):
        if name.startswith('_meta'):
            return super().__setattr__(name, value)
        name = self._meta_join_names(self._meta_name, name)
        self._meta_add_update('__setattr__', name, value)
        self._meta_name = None

    def __call__(self, *args, **kwargs):
        if self._meta_name is None:
            raise TypeError(
                'Object "{self}" is not callable'.format(self=self))
        self._meta_add_update(self._meta_name, *args, **kwargs)
        self._meta_name = None
        return self

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

    # Protected

    _meta_TaskUpdate = TaskUpdate

    def _meta_join_names(self, *names):
        return '.'.join(filter(None, names))

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
