import inspect
from .task import Task

class DescriptorTask(Task):
    
    #Public
    
    def __init__(self, descriptor):
        self._descriptor = descriptor
 
    def invoke(self):
        return self._descriptor.__get__(
            self.meta_module, type(self.meta_module))
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._descriptor))