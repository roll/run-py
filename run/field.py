import inspect
import importlib

class Field:
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.__binding = None
        self.__params = kwargs
    
    def __get__(self, module, module_class=None):
        if not self.__binding:
            pacakge = inspect.getmodule(self).__package__
            module = importlib.import_module('.binding', pacakge)
            self.__binding = module.Binding(self, module, self.__params)
        if self.__binding.module != module:
            raise RuntimeError(
                'Field "{0}" is already bound to module "{1}"'.
                format(self, self._manager.module)) 
        return self
    
    def help(self):
        pass
    
    #Protected

    def _binding(self):
        if self.__binding:
            return self.__binding
        else:
            raise RuntimeError(
                'Field "{0}" is not bound to any module'.format(self))