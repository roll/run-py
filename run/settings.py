from lib31.program import Settings
from .version import version

class Settings(Settings):
    
    #Public
    
    default_path = '.'
    default_file = 'runfile.py'
    default_attribute = 'default'
    default_arguments = []
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
             'default': default_arguments,
            },       
            {
             'dest': 'file',
             'flags': ['-f', '--file'],
             'default': default_file,
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
             'dest': 'path',
             'flags': ['-p', '--path'],
             'default': default_path,
            },                      
            {
             'dest': 'recursively',
             'action': 'store_true',
             'flags': ['-r', '--recursively'],
            },                                                   
            {
             'action': 'version',
             'flags': ['-V', '--version'],
             'version': 'Run '+str(version),               
            },                                                             
        ],        
    }
    
    
settings = Settings()