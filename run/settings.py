from packgram.package import Settings
from .version import version

class Settings(Settings):
    
    #Public
    
    command_schema = {
        'prog': 'run',
        'add_help': False,                     
        'arguments': [
            {
             'name': 'task',
             'nargs': '?',
             'default': 'default',
            },
            {
             'name': 'arguments',
             'nargs':'*',
             'default': [],
            },             
            {
             'dest': 'file',
             'flags': ['-f', '--file'],
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