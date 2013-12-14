import inspect
import importlib
from lib31.python import cachedproperty

class Field:
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.__params = kwargs
        self.__module = None
    
    def __get__(self, module, module_class=None):
        if not self.__module:
            self.__module = module
        if self._binding.module != module:
            raise RuntimeError(
                'Field "{0}" is already bound to module "{1}"'.
                format(self, self._binding.module))
        return self
    
    def help(self):
        pass
    
    #Protected

    @cachedproperty
    def _binding(self):
        if self.__module:
            package = inspect.getmodule(self).__package__
            module = importlib.import_module('.binding', package)
            return module.Binding(self, self.__params, self.__module)
        else:
            raise RuntimeError(
                'Field "{0}" is not bound to any module'.format(self))