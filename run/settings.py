from lib31.package import Settings

class Settings(Settings):
    
    command_schema = {
        'config': {
            'prog': 'run',
            'add_help': False,
        },                      
        'arguments': {
            'method': {},
            'parameters': {
                'nargs':'*',
                'required': False,
            },             
        },
        'options': {        
            'server': {
                'flags': ['-s', '--server',],
                'required': True,
            },   
            'protocol': {
                'flags': ['-p', '--protocol',],
                'required': False,
            },                                     
        },        
    }
    
    default_protocol = 'run-json-1.0'    
    
    
settings = Settings()