import logging
from lib31.python import cachedproperty
from .cluster import Cluster
from .dispatcher import Dispatcher
from .failure import Failure
from .handler import CallbackHandler
from .settings import settings
from .task import Task, InitiatedTaskSignal, CompletedTaskSignal
from .var import InitiatedVarSignal, RetrievedVarSignal

class Run:
    
    #Public
    
    def __init__(self, names=[], tags=[], 
                 path=settings.default_path,
                 file_pattern=settings.default_file, 
                 recursively=False, 
                 existent=False,
                 stackless=False):
        self._names = names
        self._tags = tags
        self._path = path
        self._file_pattern = file_pattern
        self._recursively = recursively
        self._existent = existent 
        self._stackless = stackless
        self._handlers = []     
        self._stack = []
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
            path=self._path, 
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
        self._log_executed_attribute(signal.attribute)
        if not self._stackless:
            self._stack.pop()
    
    def _log_executed_attribute(self, attribute):
        if self._stackless:
            message = attribute.meta_qualname
        else:
            names = []
            previous = self._stack[0]
            names.append(previous.meta_qualname)
            for attribute in self._stack[1:]:
                current = attribute
                if current.meta_module == previous.meta_module:
                    names.append(current.meta_name)
                else:
                    names.append(current.meta_qualname) 
                previous = current
            message = '/'.join(names)
        logger=logging.getLogger('executed')
        logger.info(message)