class Field:
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self._field_require = kwargs.get('require', [])
        self._field_help = kwargs.get('help', None)
        self._field_owner = self
    
    def __get__(self, owner, owner_class=None):
        self._field_owner = owner
        return self
    
    def help(self):
        if self._field_help:
            print(self._field_help)
            
    #Protected
    
    def _field_resolve(self):
        for task_name in self._field_require:
            task = getattr(self._run_object, task_name)
            task()
            
    @property
    def _run_object(self):
        from .run import Run
        run = self._field_owner
        if isinstance(run, Run):
            return run
        else:
            raise RuntimeError('Field is not bound')
    
    @property
    def _run_fields(self):
        fields = {}
        for cls in self._run_object.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Field):
                    fields[name] = attr
        return fields
    
    @property
    def _run_modules(self):
        from .module import Module
        return [name for name, prop 
                in self._run_fields.items() 
                if isinstance(prop, Module)]
    @property
    def _run_tasks(self):
        from .task import Task
        return [name for name, prop 
                in self._run_fields.items() 
                if isinstance(prop, Task)]
    @property
    def _run_vars(self):
        from .var import Var
        return [name for name, prop 
                in self._run_fields.items() 
                if isinstance(prop, Var)]                                       