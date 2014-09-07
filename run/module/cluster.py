import os
import inspect
from box.functools import cachedproperty
from ..find import find
from ..task import ClusterTask
from .module import Module


class ClusterModule(Module):

    # Public

    def __init__(self, *args,
                 key=None, tags=None,
                 file=None, exclude=None, basedir=None, recursively=None,
                 **kwargs):
        self._key = key
        self._tags = tags
        self._file = file
        self._exclude = exclude
        self._basedir = basedir
        self._recursively = recursively
        for task_name, task_instances in self._tasks.items():
            if not hasattr(type(self), task_name):
                task = ClusterTask(task_instances, meta_module=self)
                setattr(type(self), task_name, task)
        super().__init__(*args, **kwargs)

    # Protected

    _find = find
    _Module = Module

    @property
    def _tasks(self):
        tasks = {}
        keys = set()
        for module in self._modules:
            keys.update(module.meta_tasks.keys())
        for key in keys:
            tasks[key] = []
            for module in self._modules:
                # TODO: sync with skip parameter
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
        Modules = self._find(
            target=self._Module,
            key=self._key,
            tags=self._tags,
            file=self._file,
            exclude=self._exclude,
            basedir=self._basedir,
            recursively=self._recursively,
            filters=[{'notfilepath': self._notfilepath}])
        return Modules

    @property
    def _notfilepath(self):
        notfilepath = os.path.relpath(
            inspect.getfile(type(self.meta_module)), start=self._basedir)
        return notfilepath
