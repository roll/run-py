from box.functools import cachedproperty
from ..cluster import Cluster
from ..dispatcher import Dispatcher
from ..failure import Failure
from ..settings import settings
from ..task import Task
from .controller import RunController
from .stack import RunStack

class Run:
    
    #Public
    
    default_filename = settings.default_file  
    default_basedir = settings.default_basedir
    
    def __init__(self, names=[], tags=[], 
                 filename=None, basedir=None, recursively=False, 
                 existent=False, stackless=False):
        self._names = names
        self._tags = tags
        self._filename = filename
        self._basedir = basedir
        self._recursively = recursively
        self._existent = existent 
        self._stackless = stackless
        if not self._filename:
            self._filename = self.default_filename
        if not self._basedir:
            self._basedir = self.default_basedir         
                
    def run(self, attribute, *args, **kwargs):
        try:
            self._controller.listen()
            attributes = getattr(self._cluster, attribute)
            for attribute in attributes:
                if isinstance(attribute, self._task_class):
                    result = attribute(*args, **kwargs)
                    if result:
                        self._print_function(result)
                else:
                    self._print_function(attribute)
        except self._failure_class:
            pass
        #TODO: implement
        except Exception as exception:
            raise self._failure_class(exception)
         
    #Protected
    
    _print_function = staticmethod(print)
    _task_class = Task
    _failure_class = Failure
    _controller_class = RunController
    _dispatcher_class = Dispatcher
    _cluster_class = Cluster
    _stack_class = RunStack
    
    @cachedproperty
    def _controller(self):
        return self._controller_class(
            self._dispatcher, self._stack)
    
    @cachedproperty   
    def _cluster(self):
        return self._cluster_class(
            names=self._names,
            tags=self._tags,
            filename=self._filename,
            basedir=self._basedir, 
            recursively=self._recursively,
            existent=self._existent,
            dispatcher=self._dispatcher)
    
    @cachedproperty
    def _dispatcher(self):
        return self._dispatcher_class()
       
    @cachedproperty
    def _stack(self):
        if not self._stackless:
            return self._stack_class()
        else:
            return None