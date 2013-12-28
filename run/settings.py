from lib31.program import Settings
from .version import version

class Settings(Settings):
    
    #Defaults
    
    default_attribute = 'default'
    default_arguments = []
    default_file = 'runfile.py'
    default_logging_level = 'WARNING'
    default_main_module_name = '__main__'
    default_names = []
    default_path = '.'
    default_tags = []
    
    @property
    def argparse(self):
        return {
            'prog': 'run',
            'add_help': False,            
            'arguments': [
                {
                 'name': 'attribute',
                 'nargs': '?',
                 'default': None,
                 'help': 'Attribute to process.',
                },
                {
                 'name': 'arguments',
                 'nargs':'*',
                 'default': self.default_arguments,
                 'help': 'Arguments for attribute.',
                },    
                {
                 'dest': 'debug',
                 'action': 'store_true',
                 'flags': ['-d', '--debug'],
                 'help': 'Enable debug mode.',
                }, 
                {
                 'dest': 'existent',
                 'action': 'store_true',
                 'flags': ['-e', '--existent'],
                 'help': 'Process only existen attributes.',
                }, 
                {
                 'action': 'help',
                 'flags': ['-h', '--help'],
                 'help': 'Display this help message.',                         
                },                                      
                {
                 'dest': 'info',
                 'action': 'store_true',
                 'flags': ['-i', '--info'],
                 'help': 'Display attribute information.',                 
                },                          
                {
                 'dest': 'file',
                 'flags': ['-f', '--file'],
                 'default': self.default_file,
                 'help': 'Runfile filename pattern.',                 
                },
                {
                 'dest': 'list',
                 'action': 'store_true',
                 'flags': ['-l', '--list'],
                 'help': 'Display attribute attributes.',                 
                },                          
                {
                 'dest': 'meta',
                 'action': 'store_true',
                 'flags': ['-m', '--meta'],
                 'help': 'Display attribute meta.',                 
                },
                {
                 'dest': 'names',
                 'nargs':'*',
                 'flags': ['-n', '--names'],
                 'default': self.default_names,
                 'help': 'Main modules names to match.',
                },
                {
                 'dest': 'path',
                 'flags': ['-p', '--path'],
                 'default': self.default_path,
                 'help': 'Base directory path.',
                },     
                {
                 'dest': 'quiet',
                 'action': 'store_true',
                 'flags': ['-q', '--quiet'],
                 'help': 'Enable quiet mode.',
                },                            
                {
                 'dest': 'recursively',
                 'action': 'store_true',
                 'flags': ['-r', '--recursively'],
                 'help': 'Enable finding runfiles recursively.',
                },
                {
                 'dest': 'stackless',
                 'action': 'store_true',
                 'flags': ['-s', '--stackless'],
                 'help': 'Enable stackless mode.',
                },                          
                {
                 'dest': 'tags',
                 'nargs':'*',
                 'flags': ['-t', '--tags'],
                 'default': self.default_tags,
                 'help': 'Main module tags to match.',                 
                },   
                {
                 'dest': 'verbose',
                 'action': 'store_true',
                 'flags': ['-v', '--verbose'],
                 'help': 'Enable verbose mode.',                 
                },                                                                                
                {
                 'action': 'version',
                 'flags': ['-V', '--version'],
                 'version': 'Run '+str(version),
                 'help': 'Display the program version.',                          
                },                                                             
            ],        
        }
        
    @property
    def logging(self):
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'loggers': {
                '': {
                    'handlers': ['default'],        
                    'level': self.default_logging_level,
                    'propagate': True,
                },
                'executed': {                  
                    'handlers': ['executed'], 
                    'propagate': False,  
                }                    
            },
            'handlers': {
                'default': {
                    'level':'DEBUG',    
                    'class':'logging.StreamHandler',
                    'formatter': 'default',
                },
                'executed': {
                    'level':'DEBUG',    
                    'class':'logging.StreamHandler',
                    'formatter': 'executed',                
                },        
            },
            'formatters': {
                'default': {
                    'format': '[%(levelname)s] %(name)s: %(message)s'
                },
                'executed': {
                    'format': '[+] %(message)s'
                },                       
            },
        }
    
    
settings = Settings()