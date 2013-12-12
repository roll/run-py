import inspect
from .meta import RunMeta
from .task import Task

class Run(metaclass=RunMeta):
    
    #Public
    
    def list(self):
        "Print list of tasks"
        task_names = []
        for cls in self.__class__.mro():
            for name in cls.__dict__:
                if not name.startswith('_'):
                    attr = cls.__dict__[name]
                    if isinstance(attr, Task):
                        task_names.append(name)
        print('\n'.join(sorted(task_names)))
    
    def help(self, task_name):
        "Print task's help"        
        if not task_name.startswith('_'):
            attr = getattr(self, task_name)
            if inspect.ismethod(attr):
                signature = inspect.signature(attr)
                docstring = inspect.getdoc(attr)                    
                lines = []
                lines.append(task_name+str(signature))
                if docstring:
                    lines.append(str(docstring))
                print('\n'.join(lines))
                
    default = list     