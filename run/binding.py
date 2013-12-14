from .run import Run
from .field import Field
from .module import Module
from .task import Task
from .var import Var

class Binding:
    
    #Public
    
    def __init__(self, field, field_params, module):
        self._field = field
        self._field_params = field_params
        self._module = module
    
    @property    
    def field(self):
        return self._field
    
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
    
    def resolve(self):
        for task_name in self.filed_require:
            task = getattr(self.module, task_name)
            task()                                   