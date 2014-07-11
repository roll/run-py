from box.functools import cachedproperty
from ..attribute import Attribute
from ..cluster import Cluster
from ..signal import Dispatcher
from .controller import Controller
from .stack import Stack

class Machine:
    
    #Public
    
    def __init__(self, names=None, tags=None, *, 
                 file=None, basedir=None, recursively=False, 
                 existent=False, plain=False):
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        self._existent = existent 
        self._plain = plain        
                
    def process(self, attribute, *args, **kwargs):
        self._controller.listen()
        attributes = getattr(self._cluster, attribute)
        for attribute in attributes:
            if (isinstance(attribute, self._attribute_class) and
                callable(attribute)):
                result = attribute(*args, **kwargs)
                if result:
                    self._print(result)
            else:
                self._print(attribute)
         
    #Protected
    
    _attribute_class = Attribute
    _controller_class = Controller
    _dispatcher_class = Dispatcher
    _cluster_class = Cluster
    _print = staticmethod(print)
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
            dispatcher=self._dispatcher)
    
    @cachedproperty
    def _dispatcher(self):
        return self._dispatcher_class()
       
    @cachedproperty
    def _stack(self):
        if not self._plain:
            return self._stack_class()
        else:
            return None