from .function import FunctionTask

class MethodTask(FunctionTask):
    
    #Public
    
    def __init__(self, method):
        super().__init__(method)
        
    def complete(self, *args, **kwargs):
        return self._function(self.meta_module, *args, **kwargs)