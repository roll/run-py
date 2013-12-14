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
    
    #TODO: implement
    @property    
    def field_name(self):
        pass
    
    @property    
    def field_params(self):
        return self._field_params
    
    @property 
    def field_require(self):
        return self.field_params.get('require', [])
    
    @property 
    def field_help(self):
        return self.field_params.get('help', None)
            
    @property    
    def module(self):
        return self._module
        
    @property
    def module_fields(self):
        fields = {}
        for cls in self.module.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Field):
                    fields[name] = attr
        return fields
    
    @property
    def module_modules(self):
        return [name for name, prop 
                in self.fields.items() 
                if isinstance(prop, Module)]
    @property
    def module_tasks(self):
        return [name for name, prop 
                in self.fields.items() 
                if isinstance(prop, Task)]
    @property
    def __module_vars(self):
        return [name for name, prop 
                in self.fields.items() 
                if isinstance(prop, Var)]
    
    def __resolve(self):
        for task_name in self.field_require:
            task = getattr(self.module, task_name)
            task()                            