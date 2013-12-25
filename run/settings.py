from lib31.program import Settings
from .version import version

class Settings(Settings):
    
    #Public
    
    default_runfile = 'runfile.py'
    default_attribute = 'default'
    default_main_module_name = '__main__'
    
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
             'default': default_runfile,
            },   
            {
             'dest': 'help',
             'action': 'store_true',
             'flags': ['-h', '--help'],
            },
            {
             'dest': 'meta',
             'action': 'store_true',
             'flags': ['-m', '--meta'],
            },                            
            {
             'action': 'version',
             'flags': ['-V', '--version'],
             'version': 'Run '+str(version),               
            },                                                             
        ],        
    }
    
    
settings = Settings()