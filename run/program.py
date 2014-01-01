import sys
import logging.config
from lib31.program import Program
from lib31.python import cachedproperty
from .cluster import Cluster
from .dispatcher import dispatcher
from .command import Command
from .handler import CallbackHandler
from .settings import settings
from .task import Task, InitiatedTaskSignal, CompletedTaskSignal
from .var import InitiatedVarSignal, RetrievedVarSignal

#TODO: split to Run/Program?
class Program(Program):
    
    #Public
    
    def __init__(self, argv):
        super().__init__(argv)
        self._stack = []
     
    def __call__(self):
        self._config()
        self._execute()
         
    #Protected
    
    def _config(self):
        self._config_logging()
        self._config_dispatcher()
        
    def _config_logging(self):
        logging.config.dictConfig(settings.logging)
        logger = logging.getLogger()
        if self._command.debug:
            logger.setLevel(logging.DEBUG)
        if self._command.verbose:
            logger.setLevel(logging.INFO)
        if self._command.quiet:
            logger.setLevel(logging.ERROR)      
        
    def _config_dispatcher(self):
        dispatcher.add_handler(CallbackHandler(
            self._on_initiated_attribute, 
            signals=[InitiatedTaskSignal, 
                     InitiatedVarSignal]))
        dispatcher.add_handler(CallbackHandler(
            self._on_executed_attribute, 
            signals=[CompletedTaskSignal, 
                     RetrievedVarSignal])) 
    
    #TODO: refactor
    def _execute(self):
        try:
            for attribute in self._attributes:
                if isinstance(attribute, Task):
                    result = attribute(
                        *self._command.args, **self._command.kwargs)
                    if result:
                        print(result)
                else:
                    print(attribute)
        except Exception as exception:
            #TODO: wrap in AttributeFailure
            self._logger.error(
                str(exception), exc_info=self._command.debug)
            sys.exit(1)
    
    @cachedproperty
    def _attributes(self):
        attributes = getattr(
            self._cluster, self._command.attribute)
        return attributes
        
    @cachedproperty   
    def _cluster(self):
        return Cluster(
            names=self._command.names,
            tags=self._command.tags,
            path=self._command.path, 
            file_pattern=self._command.file,
            recursively=self._command.recursively,
            existent=self._command.existent)
    
    @cachedproperty
    def _command(self):
        return Command(self._argv)
     
    @cachedproperty    
    def _logger(self):
        return logging.getLogger(__name__)
    
    def _on_initiated_attribute(self, signal):
        if not self._command.stackless:
            self._stack.append(signal.attribute)   

    def _on_executed_attribute(self, signal):
        self._log_executed_attribute(signal.attribute)
        if not self._command.stackless:
            self._stack.pop()
    
    def _log_executed_attribute(self, attribute):
        if self._command.stackless:
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
    
        
program = Program(sys.argv)