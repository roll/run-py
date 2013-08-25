import os
from lib31.package import Settings

class Settings(Settings):
    
    #Settings path
    PATH = os.path.expanduser('~/.run/settings.py')
    
    #Parser settings
    parser = {
        'prog': 'run',
        'add_help': False,
    }
    
    #CLI options
    options = {
        'driver': {
            'flags': ['-d', '--driver',],
            'default': '',
        },               
        'ishelp': {
            'flags': ['-h', '--help'],
            'action': 'store_true',
        },                    
        'language': {
            'flags': ['-l', '--language',],
            'default': '',
        },                          
        'runfile': {
            'flags': ['-f', '--runfile',],
            'default': 'runfile',
        },
        'runclass': {
            'flags': ['-c', '--runclass',],
            'default': 'Runclass',
        },                           
    }
    
    #CLI arguments
    arguments = {
        'function': {
            'nargs': '?',
            'default': '',
        },
        'arguments': {
            'nargs':'*',
            'default': [],
        },             
    }
 
    #Language patterns
    languages = {
        'python': '\.py$',
    }
    
    #Driver patterns
    drivers = {
        'internal': 'run.drivers.{language}.{language_capitalized}Driver',
        'external': 'run_{language}.{language_capitalized}Driver',
    }
    
    
settings = Settings()