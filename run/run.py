from lib31.python import cachedproperty
from .module import Module
from .task import Task
from .var import Var

class Run(Module):
    
    #Public
    
    #TODO: add list of vars
    def list(self):
        "Print list of tasks/vars"
        print('#Tasks')               
        print('\n'.join(sorted(self._tasks)))
        print('#Vars')                       
        print('\n'.join(sorted(self._vars)))
    
    def help(self, name):
        "Print task/var help"        
        attr = self._tasks.get(name, None) or self._vars.get(name, None)
        if attr:
            print(attr.help())
        else:
            print('No name "{0}"'.format(name))

                
    default = list
    
    #Protected
    
    @cachedproperty
    def _tasks(self):
        tasks = {}
        for cls in self.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Task):
                    tasks[name] = attr
        return tasks
    
    @cachedproperty
    def _vars(self):
        vars = {}
        for cls in self.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Var):
                    vars[name] = attr
        return vars               