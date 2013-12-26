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
            'add_help': True,            
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
                 'dest': 'debug',
                 'action': 'store_true',
                 'flags': ['-d', '--debug'],
                },                                 
                {
                 'dest': 'info',
                 'action': 'store_true',
                 'flags': ['-i', '--info'],
                },                          
                {
                 'dest': 'file',
                 'flags': ['-f', '--file'],
                 'default': self.default_file,
                },
                {
                 'dest': 'list',
                 'action': 'store_true',
                 'flags': ['-l', '--list'],
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
                 'dest': 'skip',
                 'action': 'store_true',
                 'flags': ['-s', '--skip'],
                },                            
                {
                 'dest': 'tags',
                 'nargs':'*',
                 'flags': ['-t', '--tags'],
                 'default': self.default_tags,
                },   
                {
                 'dest': 'verbose',
                 'action': 'store_true',
                 'flags': ['-v', '--verbose'],
                },                                                                                
                {
                 'action': 'version',
                 'flags': ['-V', '--version'],
                 'version': 'Run '+str(version),               
                },                                                             
            ],        
        }
    
    
settings = Settings()