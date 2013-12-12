from packgram.package import Settings
from .version import version

class Settings(Settings):
    
    command_schema = {
        'prog': 'brief',
        'arguments': [
            {        
             'dest': 'file',
             'flags': ['-f', '--file',],
             'default': 'subfile.py',
            },
            {
             'action': 'version',
             'flags': ['-v', '--version'],
             'version': 'Sub '+str(version),          
            },                       
        ],         
    }      
    
    
settings = Settings()