import os
import inspect
from pprint import pprint
from collections import OrderedDict
from ..task import Task, NullTask
from ..settings import settings
from .error import ModuleAttributeError
from .metaclass import ModuleMetaclass
from .signal import (InitiatedModuleSignal, SuccessedModuleSignal,
                     FailedModuleSignal)

class Module(Task, metaclass=ModuleMetaclass):

    # Public

    def __getattribute__(self, name):
        nested_name = None
        if '.' in name:
            # Nested name - split
            name, nested_name = name.split('.', 1)
        try:
            attribute = super().__getattribute__(name)
        except AttributeError as exception:
            # To get correct AttributeError message here
            if isinstance(exception, ModuleAttributeError):
                raise
            raise ModuleAttributeError(
                'Module "{module}" has no attribute "{name}".'.
                format(module=self, name=name))
        if nested_name is not None:
            attribute = getattr(attribute, nested_name)
        return attribute

    @property
    def meta_basedir(self):
        if self.meta_is_main_module:
            basedir = os.path.dirname(inspect.getfile(type(self)))
        else:
            basedir = self.meta_module.meta_basedir
        return self._meta_params.get('basedir', basedir)

    @meta_basedir.setter
    def meta_basedir(self, value):
        self._meta_params['basedir'] = value

    @property
    def meta_cache(self):
        return self._meta_params.get('cache',
            self.meta_module.meta_cache)

    @meta_cache.setter
    def meta_cache(self, value):
        self._meta_params['cache'] = value

    @property
    def meta_is_main_module(self):
        """Module's main module status (is main module or not).
        """
        if self.meta_module:
            return False
        else:
            return True

    def meta_invoke(self, *args, **kwargs):
        return self.default(*args, **kwargs)

    def meta_lookup(self, name):
        nested_name = None
        if '.' in name:
            # Nested name - split
            name, nested_name = name.split('.', 1)
        # TODO: add good exception text here like in __getattribute__
        task = self.meta_tasks[name]
        if nested_name is not None:
            task = task.meta_lookup(nested_name)
        return task

    @property
    def meta_main_module(self):
        if self.meta_is_main_module:
            return self
        else:
            return self.meta_module.meta_main_module

    @property
    def meta_name(self):
        if super().meta_name:
            return super().meta_name
        else:
            return self._meta_default_main_module_name

    @property
    def meta_tags(self):
        """Module's tag list.
        """
        return []

    @property
    def meta_tasks(self):
        """Module's tasks dict-like object.

        Dict contains task instances, not values.
        """
        tasks = {}
        for name, attr in vars(type(self)).items():
            if isinstance(attr, Task):
                tasks[name] = attr
        return tasks

    def list(self, task=None):
        """Print tasks.
        """
        if task is None:
            task = self
        else:
            task = self.meta_lookup(task)
        names = []
        for name in sorted(dir(task)):
            # TODO: code duplication to ModuleMetaclass.__copy__
            if name.isupper():
                continue
            if name.startswith('_'):
                continue
            if name.startswith('meta_'):
                continue
            if name in task.meta_tasks:
                nested_task = task.meta_tasks[name]
                if self._meta_color:
                    name = nested_task.meta_color_name
                else:
                    name = nested_task.meta_name
            names.append(name)
        self._meta_print('\n'.join(names))

    def info(self, task=None):
        """Print information.
        """
        if task is None:
            task = self
        else:
            task = self.meta_lookup(task)
        info = task.meta_qualname
        info += task.meta_signature
        info += '\n---\n'
        info += 'Type: ' + task.meta_type
        info += '\n'
        info += 'Dependencies: ' + str(task.meta_dependencies)
        info += '\n'
        info += 'Default arguments: ' + str(task.meta_args)
        info += '\n'
        info += 'Default keyword arguments: ' + str(task.meta_kwargs)
        info += '\n---\n'
        info += task.meta_docstring
        self._meta_print(info)

    def meta(self, task=None):
        """Print metadata.
        """
        if task is None:
            task = self
        else:
            task = self.meta_lookup(task)
        meta = OrderedDict()
        for name in sorted(dir(task)):
            if name.startswith('meta_'):
                key = name.replace('meta_', '')
                attr = getattr(task, name)
                if not inspect.ismethod(attr):
                    meta[key] = attr
        self._meta_pprint(meta)

    default = NullTask(
        meta_require=['list'],
    )

    # Protected

    _meta_color = settings.color
    _meta_failed_signal_class = FailedModuleSignal  # Overriding
    _meta_initiated_signal_class = InitiatedModuleSignal  # Overriding
    _meta_print = staticmethod(print)
    _meta_pprint = staticmethod(pprint)
    _meta_successed_signal_class = SuccessedModuleSignal  # Overriding
