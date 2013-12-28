import sys
import logging
from lib31.program import Program
from lib31.python import cachedproperty
from .cluster import Cluster
from .dispatcher import dispatcher
from .command import Command
from .handler import CallbackHandler
from .task import Task, InitiatedTaskSignal, CompletedTaskSignal
from .var import InitiatedVarSignal, RetrievedVarSignal

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
        logging.basicConfig(
            level=logging.INFO, 
            format='%(name)s: %(message)s')
        
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
            if self._command.debug:
                raise
            else:
                print('Error: '+str(exception))                    
    
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
        return Command(self.argv)
    
    def _on_initiated_attribute(self, signal):
        if not self._command.stackless:
            self._stack.append(signal.attribute)   

    def _on_executed_attribute(self, signal):
        self._log_executed_attribute(signal.attribute)
        if not self._command.stackless:
            self._stack.pop()
    
    def _log_executed_attribute(self, attribute):
        if self._command.stackless:
            message = '[+] '+attribute.meta_name
        else:
            names = []
            previous = self._stack[0]
            names.append(previous.meta_name)
            for attribute in self._stack[1:]:
                current = attribute
                if current.meta_module == previous.meta_module:
                    names.append(current.meta_attribute_name)
                else:
                    names.append(current.meta_name) 
                previous = current
            message = '[+] '+'/'.join(names)
        self._logger.info(message)
    
    #TODO: move to settings
    @cachedproperty
    def _logger(self):
        formatter = logging.Formatter('%(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger = logging.getLogger('program')
        logger.addHandler(handler)
        logger.propagate = False
        return logger    
        
        
program = Program(sys.argv)