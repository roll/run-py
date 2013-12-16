from .module import Module
from .settings import settings
from .task import Task

class Run(Module):
    
    #Public
    
    def __call__(self, attribute_name, *args, **kwargs):
        if not attribute_name:
            attribute_name = settings.default_attribute
        attribute = getattr(self, attribute_name)
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
      
    default = Task(
        require=['help'],
    )

    def list(self):
        pass

    def help(self, attribute=None):
        "Print help"
        #For help
        #print(self._parser.format_help().strip())
        #sys.exit()
        if attribute:
            prop = self.attributes.get(attribute, None)
            if prop:
                print(prop.help())
        else:
            print('\n'.join(sorted(self.attributes))) 