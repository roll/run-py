from lib31.package import Settings
from .version import version

class Settings(Settings):
    
    #Public
    
    default_protocol = 'run-json-1.0' 
    
    @property
    def command_schema(self):
        return {
            'prog': 'run',
            'add_help': False,                     
            'arguments': [
                {
                 'name': 'method',
                 'nargs': '?',
                 'default': 'list',
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
                 'dest': 'protocol', 
                 'flags': ['-p', '--protocol'],
                 'default': self.default_protocol,               
                },
                {
                 'action': 'version',
                 'flags': ['-v', '--version'],
                 'version': 'run '+str(version),               
                },                                                             
            ],        
        }
   
    
settings = Settings()