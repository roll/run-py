import os
import inspect
from pprint import pprint
from builtins import print
from collections import OrderedDict
from sugarbowl import cachedproperty
from ..settings import settings
from ..task import Task, Prototype, Module, ConvertError, convert
from .controller import Controller
from .exception import GetattrError


class Module(Task, Module):

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
        return self.meta_inspect(
            name='basedir', lookup=True, default=self.__localdir)

    @property
    def meta_compact(self):
        return self.meta_inspect(
            name='compact', lookup=True, inherit=True,
            default=settings.compact)

    @cachedproperty
    def meta_controller(self):
        """Module's controller.
        """
        controller = self.meta_inspect(
            name='controller', lookup=True, inherit=True, default=None)
        if controller is None:
            controller = Controller()
        return controller

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
                    task = attr.meta_build(
                        meta_module=self,
                        meta_plain=self.meta_plain,
                        meta_dispatcher=self.meta_dispatcher)
                    setattr(type(self), name, task)
        # Initiate directories
        self.__localdir = os.path.abspath(
            os.path.dirname(inspect.getfile(type(self))))
        # Initiate controller
        self.meta_controller.listen(self)
        return self

    @property
    def meta_default(self):
        return self.meta_inspect(
            name='default_task', lookup=True, default='list')

    @property
    def meta_fullname(self):
        if self.meta_is_main_module:
            fullname = ''
            if self.meta_key is not None:
                fullname = '[{self.meta_key}]'.format(self=self)
            return fullname
        else:
            return super().meta_fullname

    @property
    def meta_inherit(self):
        return self.meta_inspect(
            name='inherit', lookup=True, default=False)

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
            return super().meta_main_module

    def meta_path(self, *components, local=False):
        if local:
            return self.__localdir
        return super().meta_path(*components)

    def meta_run(self, __attribute=None, *args, **kwargs):
        """
        Run module attribute with args, kwargs.
        """
        if self.meta_module:
            raise RuntimeError('Can\'t run not main module.')
        attribute = self
        if __attribute is not None:
            attribute = getattr(self, __attribute)
        if not callable(attribute):
            print(attribute)
            return
        result = attribute(*args, **kwargs)
        if result is None:
            return
        if not isinstance(result, list):
            print(result)
            return
        for element in result:
            if element is not None:
                print(result)
                return

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
        return self.meta_inspect(
            name='style', lookup=True, default='module')

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
        if task is None:
            task = self
        else:
            task = self.meta_lookup(task)  # pragma: no cover TODO: remove no cover
        names = []
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
                name = nested_task.meta_format(attribute='meta_fullname')
            else:
                # TODO: code duplication with Task.meta_fullname
                separator = '.'
                if task.meta_is_main_module:
                    separator = ' '
                name = separator.join(filter(None,
                    [task.meta_fullname, name]))
            names.append(name)
        result = '\n'.join(names)
        print(result)

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
        print(info)

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
        pprint(meta)
