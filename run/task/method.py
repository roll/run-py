from .function import FunctionTask

class MethodTask(FunctionTask):
    
    #Public
    
    def complete(self, *args, **kwargs):
        return self._function(self.meta_module, *args, **kwargs)