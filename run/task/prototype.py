from copy import copy
from ..helpers import merge_dicts
from .update import Update


class Prototype:

    # Public

    def __init__(self, *args, meta_class, meta_updates=None, **kwargs):
        if meta_updates is None:
            meta_updates = []
        self.__class = meta_class
        self.__updates = copy(meta_updates)
        self.__args = args
        self.__kwargs = kwargs
        self.__name = None

    def __getattr__(self, name):
        if name.startswith('_'):
            return super().__getattribute__(name)
        name = '.'.join(filter(None, [self.__name, name]))
        self.__name = name
        return self

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return super().__setattr__(name, value)
        name = '.'.join(filter(None, [self.__name, name]))
        update = Update('__setattr__', name, value)
        self.__updates.append(update)
        self.__name = None

    def __call__(self, *args, **kwargs):
        if self.__name is None:
            raise TypeError(
                'Object "{self}" is not callable'.format(self=self))
        update = Update(self.__name, *args, **kwargs)
        self.__updates.append(update)
        self.__name = None
        return self

    def meta_fork(self, *args, **kwargs):
        """Fork task prototype with optional args, kwargs altering.

        Parameters
        ----------
        args: tuple
            Positional arguments to add to prototype's default.
        kwargs: dict
            Keyword arguments to add to prototype's default.

        Returns
        -------
        :class:`.Prototype`
            Forked prototype.

        Examples
        --------
        Usage example::

            class Module(Module):

                task1 = SomeTask()
                task2 = task1.meta_fork(param='value', meta_basedir='/path')

        In this case task2 will build as task1 copy with redefined
        meta_basedir and default keyword argument param.
        """
        updates = copy(self.__updates)
        args = self.__args + args
        kwargs = merge_dicts(self.__kwargs, kwargs)
        return type(self)(
            *args,
            meta_class=self.__class,
            meta_updates=updates,
            **kwargs)

    def meta_build(self, *args, **kwargs):
        """Build task prototype to task with optional args, kwargs altering.

        Parameters
        ----------
        module: :class:`.Module`
            Module to build prototype as task of module.

        Returns
        -------
        :class:`.Task`
            Builded task.
        """
        updates = copy(self.__updates)
        args = self.__args + args
        kwargs = merge_dicts(self.__kwargs, kwargs)
        task = self.__class.meta_create(
            *args,
            meta_updates=updates,
            **kwargs)
        if task.meta_module is None:
            # No module - update
            task.meta_update()
        return task
