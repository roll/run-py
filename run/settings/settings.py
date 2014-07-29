import os
from box.logging import Settings
from ..version import version

class Settings(Settings):

    # Main

    default_arguments = []
    default_basedir = None
    default_cache = True
    default_chdir = True
    default_exclude = None
    default_fallback = None
    default_file = 'runfile.py'
    default_main_module_name = '__main__'
    default_names = None
    default_recursively = False
    default_strict = True
    default_tags = None
    default_task = 'default'

    # Argparse

    @property
    def argparse(self):
        return self._inherit_argparse(Settings, {
            'prog': 'run',
            'add_help': False,
            'arguments': [
                {
                 'name': 'task',
                 'nargs': '?',
                 'default': None,
                 'help': 'Task to run.',
                },
                {
                 'name': 'arguments',
                 'nargs': '*',
                 'default': self.default_arguments,
                 'help': 'Arguments for task.',
                },
                {
                 'dest': 'basedir',
                 'flags': ['-b', '--basedir'],
                 'default': self.default_basedir,
                 'help': 'Base directory path.',
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
                 'dest': 'file',
                 'flags': ['-f', '--file'],
                 'default': self.default_file,
                 'help': 'Runfile name/path/pattern.',
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
                 'dest': 'names',
                 'nargs': '*',
                 'flags': ['-n', '--names'],
                 'default': self.default_names,
                 'help': 'Main modules names to match.',
                },
                {
                 'dest': 'plain',
                 'action': 'store_true',
                 'flags': ['-p', '--plain'],
                 'help': 'Enable plain mode.',
                },
                {
                 'dest': 'recursively',
                 'action': 'store_true',
                 'flags': ['-r', '--recursively'],
                 'help': 'Enable finding runfiles recursively.',
                },
                {
                 'dest': 'skip',
                 'action': 'store_true',
                 'flags': ['-s', '--skip'],
                 'help': 'Skip not existen tasks.',
                },
                {
                 'dest': 'tags',
                 'nargs': '*',
                 'flags': ['-t', '--tags'],
                 'default': self.default_tags,
                 'help': 'Main module tags to match.',
                },
                {
                 'action': 'version',
                 'flags': ['-V', '--version'],
                 'version': 'Run ' + str(version),
                 'help': 'Display the program version.',
                },
            ]
        })

    # Logging

    @property
    def logging(self):
        return self._inherit_logging(Settings, {
            'loggers': {
                'initiated': {
                    'handlers': ['initiated'],
                    'propagate': False,
                },
                'successed': {
                    'handlers': ['successed'],
                    'propagate': False,
                },
                'failed': {
                    'handlers': ['failed'],
                    'propagate': False,
                },
            },
            'handlers': {
                'initiated': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'initiated',
                },
                'successed': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'successed',
                },
                'failed': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'failed',
                },
            },
            'formatters': {
                'initiated': {
                    'format': '[.] %(message)s'
                },
                'successed': {
                    'format': '[+] %(message)s'
                },
                'failed': {
                    'format': '[-] %(message)s'
                },
            },
        })

    # Extensions

    _extensions = [
        os.path.join(os.path.expanduser('~'), '.run', 'settings.py'),
    ]


settings = Settings()
