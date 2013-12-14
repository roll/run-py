import inspect
import importlib

class Field:
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.__data_shaddow = kwargs
        self.__module_shaddow = None
    
    def __get__(self, module, module_class=None):
        if not self.__module_shaddow:
            self.__module_shaddow = module
        if self.__module != module:
            raise RuntimeError(
                'Field "{0}" is already bound to module "{1}"'.
                format(self, self.__module))
        return self

    def __getitem__(self, key):
        try:
            return getattr(self, '_Field__'+key)
        except AttributeError:
            raise KeyError(key)
    
    def help(self):
        pass
    
    #Private
    
    #TODO: implement
    @property    
    def __name(self):
        pass
    
    @property 
    def __data(self):
        return self.__data_shaddow
    
    @property    
    def __module(self):
        if self.__module_shaddow:
            return self.__module_shaddow
        else:
            raise RuntimeError(
                'Field "{0}" is not bound to any module'.format(self))    
        
    @property
    def __module_fields(self):
        fields = {}
        for cls in self.__module.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Field):
                    fields[name] = attr
        return fields
    
    @property
    def __module_modules(self):
        Module = self.__import('module', 'Module')
        return [name for name, prop 
                in self.__module_fields.items() 
                if isinstance(prop, Module)]
    @property
    def __module_tasks(self):
        Task = self.__import('task', 'Task')
        return [name for name, prop 
                in self.__module_fields.items() 
                if isinstance(prop, Task)]
    @property
    def __module_vars(self):
        Var = self.__import('var', 'Var')
        return [name for name, prop 
                in self.__module_fields.items() 
                if isinstance(prop, Var)]
            
    def __import(self, module_name, attr_name):
        package_name = inspect.getmodule(Field).__package__
        module = importlib.import_module('.'+module_name, package_name)
        attr = getattr(module, attr_name)
        return attr   
    

class DependentField(Field):  
    
    def __init__(self, *args, **kwargs):
        self._require = kwargs.pop('require', [])
        super().__init__(*args, **kwargs)
        
    def resolve(self):
        for task_name in self._require:
            task = getattr(self['module'], task_name)
            task()