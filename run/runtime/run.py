from box.functools import cachedproperty
from ..signal import Dispatcher
from ..settings import settings
from ..task import Task
from .cluster import Cluster
from .controller import Controller
from .stack import Stack

class Run:
    
    #Public
    
    default_file = settings.default_file  
    default_basedir = settings.default_basedir
    
    def __init__(self, names=None, tags=None, *, 
                 file=None, basedir=None, recursively=False, 
                 existent=False, plain=False, **find_params):
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        self._existent = existent 
        self._plain = plain        
        self._find_params = find_params
        if self._file == None:
            self._file = self.default_file
        if self._basedir == None:
            self._basedir = self.default_basedir         
                
    def run(self, attribute, *args, **kwargs):
        self._controller.listen()
        attributes = getattr(self._cluster, attribute)
        for attribute in attributes:
            if isinstance(attribute, self._task_class):
                result = attribute(*args, **kwargs)
                if result:
                    self._print(result)
            else:
                self._print(attribute)
         
    #Protected
    
    _print = staticmethod(print)
    _task_class = Task
    _controller_class = Controller
    _dispatcher_class = Dispatcher
    _cluster_class = Cluster
    _stack_class = Stack
    
    @cachedproperty
    def _controller(self):
        return self._controller_class(
            self._dispatcher, self._stack)
    
    @cachedproperty   
    def _cluster(self):
        return self._cluster_class(
            names=self._names,
            tags=self._tags,
            file=self._file,
            basedir=self._basedir, 
            recursively=self._recursively,
            existent=self._existent,
            dispatcher=self._dispatcher,
            **self._find_params)
    
    @cachedproperty
    def _dispatcher(self):
        return self._dispatcher_class()
       
    @cachedproperty
    def _stack(self):
        if not self._plain:
            return self._stack_class()
        else:
            return None