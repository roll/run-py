from copy import copy
from .update import TaskUpdate

class TaskPrototype:

    # Public

    def __init__(self, cls, updates, *args, **kwargs):
        if updates == None:
            updates = []
        super().__setattr__('_class', cls)
        super().__setattr__('_updates', updates)
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)

    def __copy__(self, *args, **kwargs):
        # Documented public wrapper in :func:`run.attribute.fork`
        eupdates = copy(self._updates)
        eargs = self._args + args
        ekwargs = self._kwargs
        ekwargs.update(kwargs)
        return type(self)(self._class, eupdates, *eargs, **ekwargs)

    def __build__(self, module):
        # Documented public wrapper in :func:`run.attribute.build`
        attribute = self._create_attribute()
        self._init_attribute(attribute, module)
        self._update_attribute(attribute)
        return attribute

    def __getattr__(self, name):
        try:
            return getattr(self._class, name)
        except AttributeError:
            raise AttributeError(
                'Prototype {self} has no attribute {name}'.
                format(self=self, name=name)) from None

    def __setattr__(self, name, value):
        self._add_update('__setattr__', name, value)

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
        self._updated.append(self._update_class(name, *args, **kwargs))

    def _create_attribute(self):
        return object.__new__(self._class)

    def _init_attribute(self, attribute, module):
        attribute.__build__(module, *self._args, **self._kwargs)

    def _update_attribute(self, attribute):
        for update in self._updates:
            update.apply(attribute)
