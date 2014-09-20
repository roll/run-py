import os
import inspect
from box.functools import cachedproperty
from ...module import Module
from ..find import find_modules
from .task import ClusterTask


# TODO: fix private/protected after cachedproperty fix
class ClusterModule(Module):

    # Public

    def __init__(self, filename=None, key=None, tags=None,
                 basedir=None, **params):
        self.__filename = filename
        self.__key = key
        self.__tags = tags
        self.__basedir = basedir
        for task_name, task_instances in self._tasks.items():
            if not hasattr(type(self), task_name):
                task = ClusterTask(task_instances, meta_module=self)
                setattr(type(self), task_name, task)

    # Protected

    @property
    def _tasks(self):
        tasks = {}
        keys = set()
        for module in self._modules:
            keys.update(module.meta_tasks.keys())
        for key in keys:
            tasks[key] = []
            for module in self._modules:
                if key in module.meta_tasks:
                    task = module.meta_tasks[key]
                    tasks[key].append(task)
        return tasks

    @cachedproperty
    def _modules(self):
        modules = []
        for Module in self._Modules:
            module = Module(meta_module=self)
            modules.append(module)
        return modules

    @cachedproperty
    def _Modules(self):
        Modules = find_modules(
            filename=self.__filename,
            key=self.__key,
            tags=self.__tags,
            basedir=self.__basedir,
            filters=[{'notfilepath': self._notfilepath}])
        return Modules

    @property
    def _notfilepath(self):
        notfilepath = os.path.relpath(
            inspect.getfile(type(self.meta_module)), start=self.__basedir)
        return notfilepath
