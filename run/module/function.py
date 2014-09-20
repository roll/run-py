from box.functools import Function
from ..task import FunctionTask
from .module import Module


class FunctionModule(Module):
    """Module with tasks from FunctionTask mapping.

    For every function (callable or box.functools.Function) in every source
    module creates :class:`.task.FunctionTask` object. It may to be
    used as regular run's tasks.

    Parameters
    ----------
    mapping: object/dict
        Functions mapping.

    Examples
    --------
    Usage example::

      >>> module = FunctionModule(os.path, meta_module=None)
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

    def __init__(self, mapping, *args, **kwargs):
        self.__mapping = mapping
        for name, function in self.__functions.items():
            if not hasattr(type(self), name):
                task = FunctionTask(function, meta_module=self)
                setattr(type(self), name, task)
        super().__init__(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self._meta_get_parameter(
            'docstring',
            inherit=False,
            default=('FunctionModule with following mapping: {mapping}'.
                     format(mapping=self.__mapping)))

    # Private

    @property
    def __functions(self):
        functions = self.__mapping
        if not isinstance(self.__mapping, dict):
            functions = {}
            for name in dir(self.__mapping):
                if name.startswith('_'):
                    continue
                attr = getattr(self.__mapping, name)
                if not callable(attr):
                    continue
                if isinstance(attr, type):
                    if not isinstance(attr, Function):
                        continue
                functions[name] = attr
        return functions
