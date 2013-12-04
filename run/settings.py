from packgram.package import Settings
from .version import version

class Settings(Settings):
    
    #Public
    
    command_schema = {
        'prog': 'run',
        'add_help': False,                     
        'arguments': [
            {
             'name': 'method',
             'nargs': '?',
             'default': None,
            },
            {
             'name': 'arguments',
             'nargs':'*',
             'default': [],
            },             
            {
             'dest': 'server',
             'flags': ['-s', '--server'],
             'default': 'runfile.py',
            },   
            {
             'dest': 'help',
             'action': 'store_true',
             'flags': ['-h', '--help'],
            },                            
            {
             'action': 'version',
             'flags': ['-v', '--version'],
             'version': 'Run '+str(version),               
            },                                                             
        ],        
    }
   
    
settings = Settings()