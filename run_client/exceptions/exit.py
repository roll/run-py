from .base import RunException

class BaseExit(RunException):
    
    def __init__(self, status=0, message='', 
                 usage=False, help=False):
        self.status = status
        self.message = message
        self.usage = usage
        self.help = help
        
    def __str__(self):
        return self.message               


class HelpExit(BaseExit):
    
    def __init__(self):
        (super(HelpExit, self).
         __init__(help=True))


class ErrorExit(BaseExit):
    
    def __init__(self, message, usage=True):
        (super(ErrorExit, self).
         __init__(status=1,
                  message=message,
                  usage=usage))
        
        
class DriverIsNotFoundExit(ErrorExit):
    
    def __init__(self, attempts, language, usage=True):
        self.attempts = attempts
        self.language = language
        (super(DriverIsNotFoundExit, self).
         __init__(message=self._message, 
                  usage=usage))
        
    @property    
    def _message(self):    
        return (
            'Driver is not found\n'
            'Attempts: {attempts}\n'
            'Language: {language}'
        ).format(
            attempts=', '.join(self.attempts),
            language=self.language           
        )
        
        
class LanguageIsNotSupportedExit(ErrorExit):
    
    def __init__(self, attempts, runfile, usage=True):
        self.attempts = attempts
        self.runfile = runfile
        (super(LanguageIsNotSupportedExit, self).
         __init__(message=self._message, 
                  usage=usage))
        
    @property    
    def _message(self):    
        return (
            'Language is not found\n'
            'Attempts: {attempts}\n'
            'Runfile: {runfile}'
        ).format(
            attempts=', '.join(self.attempts),                    
            runfile=self.runfile
        )
        
        
class RunfileIsNotFoundExit(ErrorExit):
    
    def __init__(self, attempts, patterns, dirname, 
                 basename, language, usage=True):
        self.attempts = attempts
        self.patterns = patterns
        self.dirname = dirname
        self.basename = basename
        self.language = language
        (super(RunfileIsNotFoundExit, self).
         __init__(message=self._message, 
                  usage=usage))       
    
    @property    
    def _message(self):    
        return (
            'Runfile is not found\n'
            'Attempts: {attempts}\n'
            'Patterns: {patterns} (must match all of them)\n'
            'Dirname: {dirname}\n'
            'Basename: {basename}\n'                                        
            'Language: {language}'
        ).format(
            attempts=', '.join(self.attempts),
            patterns=', '.join(self.patterns),
            dirname=self.dirname,
            basename=self.basename,                    
            language=self.language     
        )
   
        
class RunfileIsNotReadableExit(ErrorExit):
    
    def __init__(self, runfile, usage=True):
        self.runfile = runfile
        (super(RunfileIsNotReadableExit, self).
         __init__(message=self._message, 
                  usage=usage))         
    
    @property    
    def _message(self):    
        return (
            'Runfile is not readable\n'
            'Runfile: {runfile}'
        ).format(
            runfile=self.runfile
        )