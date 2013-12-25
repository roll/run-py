from lib31.program import Settings
from .version import version

class Settings(Settings):
    
    #Public
    
    default_attribute = 'default'
    default_arguments = []
    default_file = 'runfile.py'
    default_names = []
    default_path = '.'
    default_tags = []
    
    default_main_module_name = '__main__'
    
    @property
    def command_schema(self):
        return {
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
                 'default': self.default_arguments,
                },       
                {
                 'dest': 'file',
                 'flags': ['-f', '--file'],
                 'default': self.default_file,
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
                 'dest': 'names',
                 'nargs':'*',
                 'flags': ['-n', '--names'],
                 'default': self.default_names,
                },
                {
                 'dest': 'path',
                 'flags': ['-p', '--path'],
                 'default': self.default_path,
                },                      
                {
                 'dest': 'recursively',
                 'action': 'store_true',
                 'flags': ['-r', '--recursively'],
                },
                {
                 'dest': 'tags',
                 'nargs':'*',
                 'flags': ['-t', '--tags'],
                 'default': self.default_tags,
                },                                                     
                {
                 'action': 'version',
                 'flags': ['-V', '--version'],
                 'version': 'Run '+str(version),               
                },                                                             
            ],        
        }
    
    
settings = Settings()