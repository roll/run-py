class DependentAttributeDependency:
    
    #Public
    
    def __init__(self, task):
        self._unpack(task)
        self._is_resolved = False
        
    def resolve(self, attribute):
        task = getattr(attribute.meta_module, self.name)
        result = task(*self.args, **self.kwargs)
        self._is_resolved = True
        return result
    
    @property
    def name(self):
        return self._name
    
    @property
    def args(self):
        return self._args
    
    @property
    def kwargs(self):
        return self._kwargs
    
    @property
    def is_resolved(self):
        return self._is_resolved
    
    #Protected
    
    #TODO: indefinite behaviour with type error 
    #like task=('task', {'kwarg': 'kwarg'}) for example
    #Or it will be solved in new require/trigger style 
    def _unpack(self, task):
        self._name = ''
        self._args = ()
        self._kwargs = {}
        if isinstance(task, tuple):
            try:
                self._name = task[0]
                self._args = task[1]
                self._kwargs = task[2]
            except IndexError:
                pass
        else:
            self._name = task