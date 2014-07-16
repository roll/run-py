from box.functools import Function
from ..task import FunctionTask
from .module import Module

class AutoModule(Module):
    """Module with auto generated tasks from sources.

    :param list sources: python objects with attributes include functions

    For every function (callable or box.functools.Function) in every source
    module creates :class:`run.task.FunctionTask` object. It may to be
    used as regular run's tasks::

      >>> module = AutoModule([os.path], meta_module=None)
      >>> module.list()
      abspath
      ...
      splitext
      >>> module.info('basename')
      basename(p)
      ...
      Returns the final component of a pathname
      >>> module.basename('dir/file.py')
      'file.py'
    """

    # Public

    def __init__(self, sources=[]):
        self._sources = sources + self._default_sources
        for task_name, task_function in self._functions.items():
            if not hasattr(type(self), task_name):
                task = FunctionTask(task_function, meta_module=self)
                setattr(type(self), task_name, task)

    @property
    def meta_docstring(self):
        return self._meta_params.get('docstring',
            ('AutoModule with following sources: {sources}'.
             format(sources=self._sources)))

    # Protected

    _default_sources = []

    @property
    def _functions(self):
        functions = {}
        for obj in reversed(self._sources):
            for name in dir(obj):
                if name.startswith('_'):
                    continue
                attr = getattr(obj, name)
                if not callable(attr):
                    continue
                if isinstance(attr, type):
                    if not isinstance(attr, Function):
                        continue
                functions[name] = attr
        return functions
