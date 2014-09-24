import os
import inspect
from box.functools import cachedproperty
from ...module import Module
from ..find import find_modules
from .task import ClusterTask


class ClusterModule(Module):

    # Public

    def __init__(self, filename=None, key=None, tags=None,
                 basedir=None, **params):
        self.__filename = filename
        self.__key = key
        self.__tags = tags
        self.__basedir = basedir
        for task_name, task_instances in self.__tasks.items():
            if not hasattr(type(self), task_name):
                task = ClusterTask(task_instances, meta_module=self)
                setattr(type(self), task_name, task)

    # Private

    @property
    def __tasks(self):
        tasks = {}
        keys = set()
        for module in self.__modules:
            keys.update(module.meta_tasks.keys())
        for key in keys:
            tasks[key] = []
            for module in self.__modules:
                if key in module.meta_tasks:
                    task = module.meta_tasks[key]
                    tasks[key].append(task)
        return tasks

    @cachedproperty
    def __modules(self):
        modules = []
        for Module in self.__Modules:
            module = Module(meta_module=self)
            modules.append(module)
        return modules

    @cachedproperty
    def __Modules(self):
        Modules = find_modules(
            filename=self.__filename,
            key=self.__key,
            tags=self.__tags,
            basedir=self.__basedir,
            filters=[{'notfilepath': self.__notfilepath}])
        return Modules

    @property
    def __notfilepath(self):
        notfilepath = os.path.relpath(
            inspect.getfile(type(self.meta_module)), start=self.__basedir)
        return notfilepath
