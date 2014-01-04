from lib31.python import cachedproperty
from .cluster import Cluster
from .controller import Controller
from .dispatcher import Dispatcher
from .failure import Failure
from .settings import settings
from .task import Task

class Run:
    
    #Public
    
    def __init__(self, names=[], tags=[], 
                 basedir=None, file_pattern=None, recursively=False, 
                 existent=False, stackless=False):
        self._names = names
        self._tags = tags
        self._input_basedir = basedir
        self._input_file_pattern = file_pattern
        self._recursively = recursively
        self._existent = existent 
        self._stackless = stackless
                
    def run(self, attribute, *args, **kwargs):
        try:
            self._controller.listen()
            attributes = getattr(self._cluster, attribute)
            for attribute in attributes:
                if isinstance(attribute, self._task_class):
                    result = attribute(*args, **kwargs)
                    if result:
                        self._print_operator(result)
                else:
                    self._print_operator(attribute)
        except self._failure_class:
            pass
        #TODO: implement
        except Exception as exception:
            raise self._failure_class(exception)
         
    #Protected
    
    _print_operator = staticmethod(print)
    _default_basedir = settings.default_basedir
    _default_file_pattern = settings.default_file  
    _task_class = Task
    _failure_class = Failure
    _controller_class = Controller
    _dispatcher_class = Dispatcher
    _cluster_class = Cluster
    
    @cachedproperty
    def _controller(self):
        return self._controller_class(
            self._dispatcher, stackless=self._stackless)
    
    @cachedproperty
    def _dispatcher(self):
        return self._dispatcher_class()
    
    @cachedproperty   
    def _cluster(self):
        return self._cluster_class(
            names=self._names,
            tags=self._tags,
            basedir=self._basedir, 
            file_pattern=self._file_pattern,
            recursively=self._recursively,
            existent=self._existent,
            dispatcher=self._dispatcher)
    
    @property
    def _basedir(self):
        if self._input_basedir:
            return self._input_basedir
        else:
            return self._default_basedir
        
    @property
    def _file_pattern(self):
        if self._input_file_pattern:
            return self._input_file_pattern
        else:
            return self._default_file_pattern    