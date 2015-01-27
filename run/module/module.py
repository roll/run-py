import os
import inspect
from pprint import pprint
from builtins import print
from collections import OrderedDict
from ..helpers import cachedproperty, import_object
from ..settings import settings
from ..task import Task, Prototype, ConvertError, convert, stylize
from .exception import GetattrError


class Module(Task):

    # Public

    Auto = True

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
    def Basedir(self):
        default = os.path.abspath(
            os.path.dirname(inspect.getfile(type(self))))
        return self.Inspect('Basedir', default=default)

    @property
    def Cache(self):
        """Vars caching status (enabled or disabled).
        """
        return self.Inspect('Cache', default=settings.cache)

    @classmethod
    def Create(cls, *args, **kwargs):
        # Create module object
        spawned_class = cls.Spawn()
        self = super(Module, spawned_class).Create(*args, **kwargs)
        # Create tasks
        names = []
        for cls in type(self).mro():
            for name, attr in vars(cls).items():
                if name in names:
                    continue
                names.append(name)
                if isinstance(attr, Prototype):
                    task = attr.Build(Module=self)
                    setattr(type(self), name, task)
        return self

    @property
    def Default(self):
        return self.Inspect('Default', default='list')

    def Invoke(self, *args, **kwargs):
        default = getattr(self, self.Default)
        result = default(*args, **kwargs)
        return result

    @cachedproperty
    def Listeners(self):
        listeners = self.Inspect('Listeners')
        if listeners is None:
            listeners = []
            if not self.Module:
                for pointer in settings.listeners:
                    element = import_object(pointer)
                    listener = element()
                    listeners.append(listener)
        return listeners

    def Inspect(self, name, *, module=False, default=None):
        """Return meta parameter
        """
        return super().Inspect(name, default=default)

    @classmethod
    def Spawn(cls):
        names = []
        attrs = {}
        for namespace in cls.mro():
            for name, attr in vars(namespace).items():
                if name in names:
                    continue
                names.append(name)
                if name[0].isupper():
                    continue
                elif name.startswith('_'):
                    continue
                elif isinstance(attr, Prototype):
                    attrs[name] = attr.Fork()
                else:
                    if cls.Auto:
                        try:
                            attrs[name] = convert(attr)
                        except ConvertError:
                            pass
        attrs['__doc__'] = cls.__doc__
        attrs['__module__'] = cls.__module__
        return type(cls)(cls.__name__, (cls,), attrs)

    @property
    def Style(self):
        return self.Inspect('Style', default='module')

    @property
    def Tasks(self):
        """Module's tasks dict-like object.

        Dict contains task instances, not values.
        """
        tasks = {}
        for name, attr in vars(type(self)).items():
            if isinstance(attr, Task):
                tasks[name] = attr
        return tasks

    def Update(self):
        for task in self.Tasks.values():
            task.Update()
        super().Update()

    def list(self, module=None):
        """Print module tasks.
        """
        # TODO: exception here breaks system tests. Why???
        # Example:
        # raise Exception()
        names = []
        module = self.__get_task(module)
        for name in sorted(dir(module)):
            # TODO: code duplication with ModuleMetaclass.Spawn
            if name[0].isupper():
                continue
            elif name.startswith('_'):
                continue
            elif name in module.Tasks:
                task = module.Tasks[name]
                if task.Hidden:
                    continue
                name = stylize(task.Qualname, style=task.Style)
            else:
                name = '.'.join(filter(None, [module.Qualname, name]))
            names.append(name)
        result = '\n'.join(names)
        print(result)

    def info(self, task=None):
        """Print task information.
        """
        info = ''
        task = self.__get_task(task)
        info += task.Qualname
        info += task.Signature
        info += '\n---\n'
        info += 'Type: ' + task.Type
        info += '\n'
        info += 'Dependencies: ' + str(task.Dependencies)
        info += '\n'
        info += 'Default arguments: ' + str(task.Args)
        info += '\n'
        info += 'Default keyword arguments: ' + str(task.Kwargs)
        info += '\n---\n'
        info += task.Docstring
        print(info)

    def meta(self, task=None):
        """Print task metadata.
        """
        meta = OrderedDict()
        task = self.__get_task(task)
        for name in sorted(dir(task)):
            if name[0].isupper():
                attr = getattr(task, name)
                if not inspect.ismethod(attr):
                    meta[name] = attr
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
        task = self.Tasks[name]
        if nested_name is not None:
            task = task.__get_task(nested_name)
        return task
