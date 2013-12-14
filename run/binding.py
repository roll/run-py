from .run import Run
from .field import Field
from .module import Module
from .task import Task
from .var import Var

class Binding:
    
    #Public
    
    def __init__(self, field, owner, params):
        self._field = field
        self._owner = owner
        self._params = params
    
    @property    
    def field(self):
        return self._field
    
    @property    
    def owner(self):
        return self._owner   
     
    @property 
    def require(self):
        return self._field_params.get('require', [])
    
    @property 
    def help(self):
        return self._field_params.get('help', None)    
    
    def resolve(self):
        for task_name in self.require:
            task = getattr(self.run, task_name)
            task()
                  
    @property
    def run(self):
        run = self.owner
        if isinstance(run, Run):
            return run
        else:
            raise RuntimeError('Field is not bound')
    
    @property
    def fields(self):
        fields = {}
        for cls in self.run.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Field):
                    fields[name] = attr
        return fields
    
    @property
    def modules(self):
        return [name for name, prop 
                in self.fields.items() 
                if isinstance(prop, Module)]
    @property
    def tasks(self):
        return [name for name, prop 
                in self.fields.items() 
                if isinstance(prop, Task)]
    @property
    def vars(self):
        return [name for name, prop 
                in self.fields.items() 
                if isinstance(prop, Var)]                                       