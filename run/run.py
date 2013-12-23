from .module import ModuleMeta, Module
from .settings import settings
from .task import Task

class RunMeta(ModuleMeta):

    #Public
    
    def __call__(self, *args, **kwargs):
        if 'module' not in kwargs:
            kwargs['module'] = None
        return super().__call__(*args, **kwargs)
    

class Run(Module, metaclass=RunMeta):
    
    #Public
    
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
        for attribute in sorted(self.attributes):
            print(attribute)

    def help(self, attribute):
        "Print attribute help"
        if attribute in self.attributes:
            print(self.attributes[attribute].metadata.help)
        else:
            raise RuntimeError('No attribute "{0}"'.format(attribute))
      
    default = Task(
        require=['list'],
    )        