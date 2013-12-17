from .module import Module
from .settings import settings
from .task import Task

class Run(Module):
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        builder = super().__new__(cls, *args, **kwargs)
        obj = builder()
        return obj
       
    def __call__(self, attribute, *args, **kwargs):
        if not attribute:
            attribute = settings.default_attribute
        attribute = getattr(self, attribute)
        if callable(attribute):
            result = attribute(*args, **kwargs)
            return result
        else:
            return attribute
    
    @property
    def runname(self):
        return ''
    
    @property
    def runtags(self):
        return []

    def list(self):
        "List attributes"
        for attribute in self.attributes:
            print(attribute)

    def help(self, attribute):
        "Print attribute help"
        if attribute in self.attributes:
            print(self.attributes[attribute].attrhelp)
        else:
            raise RuntimeError('No attribute "{0}"'.format(attribute))
      
    default = Task(
        require=['list'],
    )        