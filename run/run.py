from .module import Module
from .task import Task

class Run(Module):
    
    #Public
    
    def __call__(self, attribute_name, *args, **kwargs):
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

    def help(self, name=None):
        "Print help"
        #For help
        #print(self._parser.format_help().strip())
        #sys.exit()
        if name:
            prop = self.attributes.get(name, None)
            if prop:
                print(prop.help())
        else:
            print('\n'.join(sorted(self.attributes)))    