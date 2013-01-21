import os
from run import settings

class Process(object):
     
    @property            
    def cwd(self):
        return os.getcwd()
    
    @cwd.setter
    def cwd(self, value):
        os.chdir(value)
        

process = Process()


class CLICommand(object):
    
    def __init__(self):
        self.command = 'run'
        self.driver = 'run_python.PythonDriver'
        self.language = 'python'           
        self.ishelp = False        
        self.runfile = 'runfile.py'
        self.runclass = 'Runclass'
        self.function = 'function'
        self.arguments = ['argument1', 'argument2']
    
    @property
    def argv(self):
        return (self.cli_arguments + 
                self.cli_options)
          
    @property
    def cli_arguments(self):
        return ([arg for arg in [self.command, self.function] if arg]+
                self.arguments if self.arguments else []) 
          
    @property
    def cli_options(self):
        options = []
        for name in settings.options:
            value = getattr(self, name)
            short = settings.options[name]['flags'][0]
            if value:
                if name in ['ishelp']:
                    value = ''
                options.append(('{short}{value}'.
                                format(short=short,
                                       value=value)))
        return options
    
    
clicommand = CLICommand()