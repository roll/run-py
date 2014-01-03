import sys
import logging.config
from lib31.program import Program
from lib31.python import cachedproperty
from .command import Command
from .run import Run
from .settings import settings

class Program(Program):
    
    #Public
     
    def __call__(self):
        self._config()
        self._execute()
         
    #Protected
    
    #TODO: remove hardcoded logging, settings.logging
    def _config(self):
        logging.config.dictConfig(settings.logging)        
        logger = logging.getLogger()
        if self._command.debug:
            logger.setLevel(logging.DEBUG)
        if self._command.verbose:
            logger.setLevel(logging.INFO)
        if self._command.quiet:
            logger.setLevel(logging.ERROR)      
    
    def _execute(self):
        try:
            self._run.run(
                self._command.attribute, 
                *self._command.args, 
                **self._command.kwargs)
        except Exception as exception:
            self._logger.error(
                str(exception), exc_info=self._command.debug)
            sys.exit(1)
    
    @cachedproperty
    def _command(self):
        return Command(self._argv)
            
    @cachedproperty   
    def _run(self):
        return Run(
            names=self._command.names,
            tags=self._command.tags,
            basedir=self._command.basedir, 
            file_pattern=self._command.file,
            recursively=self._command.recursively,
            existent=self._command.existent,
            stackless=self._command.stackless)
     
    @cachedproperty    
    def _logger(self):
        return logging.getLogger(__name__)
    
        
program = Program(sys.argv)