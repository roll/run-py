from box.collections import Settings
from ..metadata import version


class Settings(Settings):

    # Main

    cache = True
    chdir = True
    compact = False
    convert = True
    fallback = None
    filename = 'runfile.py'
    inherit = False
    plain = False
    strict = True

    # Converters

    converters = [
        # Short 'run.module' doesn't work
        # in shell for nosetests
        'run.module.module',
        'run.task.task',
        'run.var.var',
    ]

    # Events

    events = {
        'failed': '[-] ',
        'successed': '[+] ',
    }

    # Styles

    styles = {
        'failed': {'foreground': 'red'},
        'successed': {'foreground': 'green'},
        'module': {'foreground': 'bright_cyan'},
        'task': {'foreground': 'bright_green'},
        'var': {'foreground': 'bright_blue'},
    }

    # Argparse

    @property
    def argparse(self):
        return {
            'prog': 'run',
            'add_help': False,
            'arguments': [
                {
                 'name': 'attribute',
                 'nargs': '?',
                 'help': 'Attribute to run.',
                },
                {
                 'name': 'arguments',
                 'nargs': '*',
                 'help': 'Arguments for attribute.',
                },
                {
                 'dest': 'compact',
                 'action': 'store_true',
                 'flags': ['-c', '--compact'],
                 'help': 'Enable compact mode.',
                },
                {
                 'dest': 'debug',
                 'action': 'store_true',
                 'flags': ['-d', '--debug'],
                 'help': 'Enable debug mode.',
                },
                {
                 'dest': 'filepath',
                 'flags': ['-f', '--filepath'],
                 'default': self.filename,
                 'help': 'Runfile path.',
                },
                {
                 'action': 'help',
                 'flags': ['-h', '--help'],
                 'help': 'Display this help message.',
                },
                {
                 'dest': 'info',
                 'action': 'store_true',
                 'flags': ['-i', '--info'],
                 'help': 'Display task information.',
                },
                {
                 'dest': 'list',
                 'action': 'store_true',
                 'flags': ['-l', '--list'],
                 'help': 'Display module tasks.',
                },
                {
                 'dest': 'meta',
                 'action': 'store_true',
                 'flags': ['-m', '--meta'],
                 'help': 'Display task meta.',
                },
                {
                 'dest': 'plain',
                 'action': 'store_true',
                 'flags': ['-p', '--plain'],
                 'help': 'Activate plain mode.',
                },
                {
                 'dest': 'quiet',
                 'action': 'store_true',
                 'flags': ['-q', '--quiet'],
                 'help': 'Enable quiet mode.',
                },
                {
                 'dest': 'verbose',
                 'action': 'store_true',
                 'flags': ['-v', '--verbose'],
                 'help': 'Enable verbose mode.',
                },
                {
                 'action': 'version',
                 'flags': ['-V', '--version'],
                 'version': 'Run ' + str(version),
                 'help': 'Display the program version.',
                },
            ]
        }

    # Logging

    logging_level = 'WARNING'
    logging_format = '[%(levelname)s] %(message)s'

    @property
    def logging_config(self):
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': self.logging_level,
                    'propagate': True,
                },
                'task': {
                    'handlers': ['task'],
                    'propagate': False,
                },
            },
            'handlers': {
                'default': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                },
                'task': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'task',
                },
            },
            'formatters': {
                'default': {
                    'format': self.logging_format
                },
                'task': {
                    'format': '%(message)s'
                },
            },
        }


settings = Settings()
