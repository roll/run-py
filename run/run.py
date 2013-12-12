import inspect
from collections import OrderedDict
from lib31.python import cachedproperty, OrderedClassMeta
from abc import ABCMeta
from .task import Task
from .var import Var

class RunMeta(OrderedClassMeta):
    
    #Public
    
    pass


class Run(metaclass=RunMeta):
    
    #Public
    
    def list(self):
        "Print list of methods"
        methods = []
        for method in dir(self):
            if not method.startswith('_'):
                attr = getattr(self, method)
                if inspect.ismethod(attr):
                    methods.append(method)
        print('\n'.join(methods))
    
    def help(self, method):
        "Print method's help"        
        if not method.startswith('_'):
            attr = getattr(self, method)
            if inspect.ismethod(attr):
                signature = inspect.signature(attr)
                docstring = inspect.getdoc(attr)                    
                lines = []
                lines.append(method+str(signature))
                if docstring:
                    lines.append(str(docstring))
                print('\n'.join(lines))
    
    def make(self):
        for task in self._tasks.values():
            task.complete(self._vars)

    #Protected
    
    @cachedproperty
    def _tasks(self):
        tasks = OrderedDict()
        for cls in reversed(self.__class__.mro()):
            for name in cls.__dict__.get('__order__', []):
                if not name.startswith('_'):
                    attr = getattr(self, name)
                    if isinstance(attr, Task):
                        tasks[name] = attr
                        tasks.move_to_end(name)
        return tasks
                        
    @cachedproperty
    def _vars(self):
        vars = {}
        for name in dir(self):
            if not name.startswith('_'):
                attr = getattr(self, name)
                if not isinstance(attr, Task):
                    if isinstance(attr, Var):
                        attr = attr.get()
                    vars[name] = attr
        return vars                