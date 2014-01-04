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
                 basedir=None, file_pattern=None, recursively=False, 
                 existent=False, stackless=False):
        self._names = names
        self._tags = tags
        self._input_basedir = basedir
        self._input_file_pattern = file_pattern
        self._recursively = recursively
        self._existent = existent 
        self._stackless = stackless
        self._config()
                
    def run(self, attribute, *args, **kwargs):
        try:
            attributes = getattr(self._cluster, attribute)
            for attribute in attributes:
                if isinstance(attribute, self._task_class):
                    result = attribute(*args, **kwargs)
                    if result:
                        self._print_operator(result)
                else:
                    self._print_operator(attribute)
        except Failure:
            pass
        #TODO: implement
        except Exception as exception:
            raise Failure(exception)
         
    #Protected
    
    _print_operator = staticmethod(print)
    _task_class = Task
    _dispatcher_class = Dispatcher
    _cluster_class = Cluster
    _callback_handler_class = CallbackHandler
    _initiated_task_signal_class = InitiatedTaskSignal
    _initiated_var_signal_class = InitiatedVarSignal
    _completed_task_signal_class = CompletedTaskSignal
    _retrieved_var_signal_class = RetrievedVarSignal
    _default_basedir = settings.default_basedir
    _default_file_pattern = settings.default_file        
    _logging_module = logging
    _stack_class = Stack
    
    def _config(self):
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_initiated_attribute, 
                signals=[self._initiated_task_signal_class, 
                         self._initiated_var_signal_class]))
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_executed_attribute, 
                signals=[self._completed_task_signal_class, 
                         self._retrieved_var_signal_class])) 
 
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
    
    def _on_initiated_attribute(self, signal):
        if not self._stackless:
            self._stack.push(signal.attribute)   

    def _on_executed_attribute(self, signal):
        if not self._stackless:
            message = str(self._stack)
            self._stack.pop()            
        else:
            message = signal.attribute.meta_qualname            
        logger=self._logging_module.getLogger('executed')
        logger.info(message)
        
    @cachedproperty
    def _stack(self):
        return self._stack_class()         