from lib31.package import Settings

class Settings(Settings):
    
    command_schema = {
        'config': {
            'prog': 'run',
            'add_help': False,
        },                      
        'arguments': {
            'function': {
                'nargs': '?',
                'default': '',
            },
            'arguments': {
                'nargs':'*',
                'default': [],
            },             
        },
        'options': {        
            'file': {
                'flags': ['-f', '--file',],
                'default': 'runfile.py',
            },
            'help': {
                'flags': ['-h', '--help'],
                'action': 'store_true',
            },                      
        },         
    }
    
    
settings = Settings()