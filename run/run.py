from .module import Module
from .settings import settings
from .task import Task

class Run(Module):
    
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
    def run_name(self):
        return ''
    
    @property
    def run_tags(self):
        return []

    def list(self):
        for attribute in self.attributes:
            print(attribute)

    def help(self, attribute):
        "Print attribute help"
        if attribute in self.attributes:
            print(self.attributes[attribute].unit_help)
        else:
            raise RuntimeError('No attribute "{0}"'.format(attribute))
      
    default = Task(
        require=['list'],
    )        