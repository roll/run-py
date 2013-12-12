import inspect
from .meta import RunMeta

class Run(metaclass=RunMeta):
    
    #Public
    
    def list(self):
        "Print list of tasks"
        tasks = []
        for task in dir(self):
            if not task.startswith('_'):
                attr = getattr(self, task)
                if inspect.ismethod(attr):
                    tasks.append(task)
        print('\n'.join(tasks))
    
    def help(self, task):
        "Print task's help"        
        if not task.startswith('_'):
            attr = getattr(self, task)
            if inspect.ismethod(attr):
                signature = inspect.signature(attr)
                docstring = inspect.getdoc(attr)                    
                lines = []
                lines.append(task+str(signature))
                if docstring:
                    lines.append(str(docstring))
                print('\n'.join(lines))
                
    default = list         