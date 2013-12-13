class Field:
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self._require = kwargs.get('require', [])
        self._help = kwargs.get('help', None)
    
    #TODO: is it safe to use Run/Module as descriptor?
    def __get__(self, owner, owner_class=None):
        self._owner = owner
        return self
    
    def help(self):
        if self._help:
            print(self._help)
            
    #Protected
    
    def _resolve(self):
        for task_name in self._require:
            task = getattr(self._run, task_name)
            task()
            
    @property
    def _run(self):
        return self._owner            