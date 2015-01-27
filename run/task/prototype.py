from copy import copy
from ..helpers import merge_dicts
from .update import Update


class Prototype:

    # Public

    def __init__(self, *args, Class, Updates=None, **kwargs):
        if Updates is None:
            Updates = []
        self.__class = Class
        self.__updates = copy(Updates)
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

    def Fork(self, *args, **kwargs):
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
                task2 = task1.Fork(param='value', Basedir='/path')

        In this case task2 will build as task1 copy with redefined
        Basedir and default keyword argument param.
        """
        updates = copy(self.__updates)
        args = self.__args + args
        kwargs = merge_dicts(self.__kwargs, kwargs)
        return type(self)(
            *args,
            Class=self.__class,
            Updates=updates,
            **kwargs)

    def Build(self, *args, **kwargs):
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
        task = self.__class.Create(
            *args,
            Updates=updates,
            **kwargs)
        if task.Module is None:
            # No module - update
            task.Update()
        return task
