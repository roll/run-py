from lib31.package import Settings

class Settings(Settings):
    
    command_schema = {
        'config': {
            'prog': 'run',
            'add_help': False,
        },                      
        'arguments': {
            'method': {},
            'arguments': {
                'nargs':'*',
                'default': [],
            },             
        },
        'options': {        
            'server': {
                'flags': ['-s', '--server',],
                'required': True,
            },                    
        },        
    }
    
    default_protocol = 'run-json-1.0'    
    
    
settings = Settings()