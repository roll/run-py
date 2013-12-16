from packgram.package import Settings
from .version import version

class Settings(Settings):
    
    #Public
    
    default_attribute = 'default'
    
    command_schema = {
        'prog': 'run',
        'add_help': False,            
        'arguments': [
            {
             'name': 'attribute',
             'nargs': '?',
             'default': None,
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
             'flags': ['-V', '--version'],
             'version': 'Run '+str(version),               
            },                                                             
        ],        
    }
   
    
settings = Settings()