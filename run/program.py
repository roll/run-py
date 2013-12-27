import sys
import logging
from lib31.program import Program
from lib31.python import cachedproperty
from .cluster import Cluster
from .dispatcher import dispatcher
from .command import Command
from .task import Task, CompletedTaskSignal

class Program(Program):
    
    #Public
     
    def __call__(self):
        self._config()
        self._execute()
         
    #Protected
    
    def _config(self):
        dispatcher.add_handler(
            self._on_completed_attribute, bases=[CompletedTaskSignal])
        logging.basicConfig(
            level=logging.INFO, 
            format='%(name)s: %(message)s')
    
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
    
    def _on_completed_attribute(self):
        print('_on_completed_attribute')   
    
    
class ProgramStack(list):
    
    #Public
    
    pass 
    
        
program = Program(sys.argv)