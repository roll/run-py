import os
import inspect
from pprint import pprint
from builtins import print
from collections import OrderedDict
from sugarbowl import cachedproperty, import_object
from ..settings import settings
from ..task import Task, Prototype, ConvertError, convert
from ..utils import stylize
from .exception import GetattrError


class Module(Task):

    # Public

    meta_convert = settings.convert
    meta_key = None
    meta_tags = []

    def __getattribute__(self, name):
        nested_name = None
        if '.' in name:
            # Nested name - split
            name, nested_name = name.split('.', 1)
        try:
            attribute = super().__getattribute__(name)
        except AttributeError as exception:
            # To get correct AttributeError message here
            if isinstance(exception, GetattrError):
                raise  # pragma: no cover TODO: remove no cover
            raise GetattrError(
                'Module "{self}" has no attribute "{name}".'.
                format(self=self, name=name))
        if nested_name is not None:
            attribute = getattr(attribute, nested_name)
        return attribute

    @property
    def meta_basedir(self):
        return self.meta_retrieve('basedir', default=self.__localdir)

    @property
    def meta_cache(self):
        """Vars caching status (enabled or disabled).
        """
        return self.meta_retrieve('cache', default=settings.cache)

    @classmethod
    def meta_create(cls, *args, **kwargs):
        # Create module object
        spawned_class = cls.meta_spawn()
        self = super(Module, spawned_class).meta_create(*args, **kwargs)
        # Create tasks
        names = []
        for cls in type(self).mro():
            for name, attr in vars(cls).items():
                if name in names:
                    continue
                names.append(name)
                if isinstance(attr, Prototype):
                    task = attr.meta_build(meta_module=self)
                    setattr(type(self), name, task)
        # Initiate directories
        self.__localdir = os.path.abspath(
            os.path.dirname(inspect.getfile(type(self))))
        return self

    @property
    def meta_default(self):
        return self.meta_retrieve('default', default='list')

    def meta_invoke(self, *args, **kwargs):
        default = getattr(self, self.meta_default)
        result = default(*args, **kwargs)
        return result

    @property
    def meta_is_main_module(self):
        """Module's main module status (is main module or not).
        """
        if self.meta_module:
            return False
        else:
            return True

    # TODO: wrong order
    @cachedproperty
    def meta_listeners(self):
        default = []
        if self.meta_is_main_module:
            for pointer in settings.listeners:
                element = import_object(pointer)
                listener = element()
                default.append(listener)
        listeners = self.meta_retrieve('listeners', default=default)
        return listeners

    def meta_path(self, *components, local=False):
        if local:
            return self.__localdir
        return super().meta_path(*components)

    @classmethod
    def meta_spawn(cls):
        names = []
        attrs = {}
        for namespace in cls.mro():
            for name, attr in vars(namespace).items():
                if name in names:
                    continue
                names.append(name)
                if name.isupper():
                    continue
                elif name.startswith('_'):
                    continue
                elif name.startswith('meta_'):
                    continue
                elif isinstance(attr, Prototype):
                    attrs[name] = attr.meta_fork()
                else:
                    if cls.meta_convert:
                        try:
                            attrs[name] = convert(attr)
                        except ConvertError:
                            pass
        attrs['__doc__'] = cls.__doc__
        attrs['__module__'] = cls.__module__
        return type(cls)(cls.__name__, (cls,), attrs)

    @property
    def meta_style(self):
        return self.meta_retrieve('style', default='module')

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

    def meta_update(self):
        for task in self.meta_tasks.values():
            task.meta_update()
        super().meta_update()

    def list(self, task=None):
        """Print tasks.
        """
        # TODO: exception here breaks system tests. Why???
        # Example:
        # raise Exception()
        names = []
        task = self.__get_task(task)
        for name in sorted(dir(task)):
            # TODO: code duplication with ModuleMetaclass.meta_spawn
            if name.isupper():
                continue  # pragma: no cover TODO: remove no cover
            elif name.startswith('_'):
                continue
            elif name.startswith('meta_'):
                continue
            elif name in task.meta_tasks:
                nested_task = task.meta_tasks[name]
                name = nested_task.meta_qualname
                name = stylize(name, styles=[nested_task.meta_style])
            else:
                name = '.'.join(filter(None, [task.meta_qualname, name]))
            names.append(name)
        result = '\n'.join(names)
        print(result)

    def info(self, task=None):
        """Print information.
        """
        info = ''
        task = self.__get_task(task)
        info += task.meta_qualname
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
        print(info)

    def meta(self, task=None):
        """Print metadata.
        """
        meta = OrderedDict()
        task = self.__get_task(task)
        for name in sorted(dir(task)):
            if name.startswith('meta_'):
                key = name.replace('meta_', '')
                attr = getattr(task, name)
                if not inspect.ismethod(attr):
                    meta[key] = attr
        pprint(meta)

    # Private

    # TODO: somehow to merge with __getattribute__?
    def __get_task(self, name=None):
        if name is None:
            return self
        nested_name = None
        if '.' in name:
            # Nested name - split
            name, nested_name = name.split('.', 1)
        # TODO: add good exception text here like in __getattribute__
        task = self.meta_tasks[name]
        if nested_name is not None:
            task = task.__get_task(nested_name)
        return task
