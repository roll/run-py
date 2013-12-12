from collections import OrderedDict
from lib31.python import cachedproperty, OrderedClassMeta
from .task import Task
from .value import Value

class SubMeta(OrderedClassMeta):
    
    #Public
    
    pass


class Sub(metaclass=SubMeta):
    
    #Public
    
    def make(self):
        for task in self._tasks.values():
            task.complete(self._values)

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
    def _values(self):
        values = {}
        for name in dir(self):
            if not name.startswith('_'):
                attr = getattr(self, name)
                if not isinstance(attr, Task):
                    if isinstance(attr, Value):
                        attr = attr.get()
                    values[name] = attr
        return values