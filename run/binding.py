from .run import Run
from .field import Field
from .module import Module
from .task import Task
from .var import Var

class Binding:
    
    #Public
    
    def __init__(self, field, module, params):
        self._field = field
        self._module = module
        self._params = params
    
    @property    
    def field(self):
        return self._field
    
    #TODO: implement
    @property    
    def field_name(self):
        pass
    
    @property    
    def module(self):
        return self._module
            
    #TODO: implement
    @property
    def module_run(self):
        pass
        
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
    def module_vars(self):
        return [name for name, prop 
                in self.fields.items() 
                if isinstance(prop, Var)]
    
    @property 
    def require(self):
        return self._params.get('require', [])
    
    @property 
    def help(self):
        return self._params.get('help', None)
    
    def resolve(self):
        for task_name in self.require:
            task = getattr(self.module, task_name)
            task()                                         