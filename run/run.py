import logging
from lib31.python import cachedproperty
from .cluster import Cluster
from .dispatcher import Dispatcher
from .failure import Failure
from .handler import CallbackHandler
from .settings import settings
from .stack import Stack
from .task import Task, InitiatedTaskSignal, CompletedTaskSignal
from .var import InitiatedVarSignal, RetrievedVarSignal

class Run:
    
    #Public
    
    def __init__(self, names=[], tags=[], 
                 basedir=settings.default_basedir,
                 file_pattern=settings.default_file, 
                 recursively=False, 
                 existent=False,
                 stackless=False):
        self._names = names
        self._tags = tags
        self._basedir = basedir
        self._file_pattern = file_pattern
        self._recursively = recursively
        self._existent = existent 
        self._stackless = stackless
        self._config()
                
    def run(self, attribute, *args, **kwargs):
        try:
            attributes = getattr(self._cluster, attribute)
            for attribute in attributes:
                if isinstance(attribute, Task):
                    result = attribute(*args, **kwargs)
                    if result:
                        print(result)
                else:
                    print(attribute)
        except Failure:
            pass
        #TODO: implement
        except Exception as exception:
            raise Failure(exception)
         
    #Protected
    
    def _config(self):
        self._dispatcher.add_handler(CallbackHandler(
            self._on_initiated_attribute, 
            signals=[InitiatedTaskSignal, 
                     InitiatedVarSignal]))
        self._dispatcher.add_handler(CallbackHandler(
            self._on_executed_attribute, 
            signals=[CompletedTaskSignal, 
                     RetrievedVarSignal])) 
        
    @cachedproperty   
    def _cluster(self):
        return Cluster(
            names=self._names,
            tags=self._tags,
            basedir=self._basedir, 
            file_pattern=self._file_pattern,
            recursively=self._recursively,
            existent=self._existent,
            dispatcher=self._dispatcher)
 
    @cachedproperty
    def _dispatcher(self):
        return Dispatcher()  
     
    def _on_initiated_attribute(self, signal):
        if not self._stackless:
            self._stack.append(signal.attribute)   

    def _on_executed_attribute(self, signal):
        if not self._stackless:
            message = self._stack.formatted
            self._stack.pop()            
        else:
            message = signal.attribute.meta_qualname            
        logger=logging.getLogger('executed')
        logger.info(message)
        
    @cachedproperty
    def _stack(self):
        return Stack()         