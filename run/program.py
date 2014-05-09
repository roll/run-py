import sys
import logging.config; logging.config #PyDev warning
from box.argparse import Program
from box.functools import cachedproperty
from .command import Command
from .run import Run
from .settings import settings

class Program(Program):
    
    #Public
     
    def __call__(self):
        self._config()
        self._execute()
         
    #Protected
    
    _logging_module = logging
    _logging_config = settings.logging
    _command_class = Command
    _run_class = Run
    
    def _config(self):
        self._logging_module.config.dictConfig(self._logging_config)        
        logger = self._logging_module.getLogger()
        if self._command.debug:
            logger.setLevel(self._logging_module.DEBUG)
        if self._command.verbose:
            logger.setLevel(self._logging_module.INFO)
        if self._command.quiet:
            logger.setLevel(self._logging_module.ERROR)      
    
    def _execute(self):
        try:
            self._run.run(
                self._command.attribute,
                *self._command.args, 
                **self._command.kwargs)
        except Exception as exception:
            self._logging_module.getLogger(__name__).error(
                self._format_exception(exception), 
                exc_info=self._command.debug)
            sys.exit(1)
    
    @cachedproperty
    def _command(self):
        return self._command_class(self._argv)
            
    @cachedproperty   
    def _run(self):
        return self._run_class(
            names=self._command.names,
            tags=self._command.tags,
            filename=self._command.file,            
            basedir=self._command.basedir, 
            recursively=self._command.recursively,
            existent=self._command.existent,
            stackless=self._command.stackless)
    
    def _format_exception(self, exception):
        return '{category}: {message}'.format(
            category=type(exception).__name__,
            message=str(exception))
    
        
program = Program(sys.argv)