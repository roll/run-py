from .module import ModuleMetaclass, Module
from .settings import settings
from .task import Task

class RunMetaclass(ModuleMetaclass):

    #Public
    
    def __call__(self, *args, **kwargs):
        if 'module' not in kwargs:
            kwargs['module'] = None
        return super().__call__(*args, **kwargs)
    

class Run(Module, metaclass=RunMetaclass):
    
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
        for attribute in sorted(self.meta_attributes):
            print(attribute)

    def help(self, attribute):
        "Print attribute help"
        if attribute in self.attributes:
            print(self.attributes[attribute].meta_help)
        else:
            raise RuntimeError('No attribute "{0}"'.format(attribute))
      
    default = Task(
        require=['list'],
    )        