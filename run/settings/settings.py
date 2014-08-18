import os
from box.logging import Settings
from ..version import version


class Settings(Settings):

    # Main

    basedir = None
    cache = True
    chdir = True
    convert = True
    fallback = None
    file = 'runfile.py'
    key = None
    plain = False
    recursively = False
    strict = True
    tags = None

    default_task = 'default'

    # Converters

    converters = [
        'run.module.module',
        'run.task.task',
        'run.var.var',
    ]

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
        return self._inherit_argparse(Settings, {
            'prog': 'run',
            'add_help': False,
            'arguments': [
                {
                 'name': 'task',
                 'nargs': '?',
                 'help': 'Task to run.',
                },
                {
                 'name': 'arguments',
                 'nargs': '*',
                 'help': 'Arguments for task.',
                },
                {
                 'dest': 'basedir',
                 'flags': ['-b', '--basedir'],
                 'default': self.basedir,
                 'help': 'Base directory path.',
                },
                {
                 'dest': 'compact',
                 'action': 'store_true',
                 'flags': ['-c', '--compact'],
                 'help': 'Enable compact mode.',
                },
                {
                 'dest': 'file',
                 'flags': ['-f', '--file'],
                 'default': self.file,
                 'help': 'Runfile name/path/pattern.',
                },
                {
                 'dest': 'plain',
                 'action': 'store_true',
                 'flags': ['-p', '--plain'],
                 'help': 'Activate plain mode.',
                },
                {
                 'action': 'help',
                 'flags': ['-h', '--help'],
                 'help': 'Display this help message.',
                },
                {
                 'dest': 'key',
                 'flags': ['-k', '--key'],
                 'default': self.key,
                 'help': 'Main module key to match.',
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
                 'default': self.tags,
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
                'task': {
                    'handlers': ['task'],
                    'propagate': False,
                },
            },
            'handlers': {
                'task': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'task',
                },
            },
            'formatters': {
                'task': {
                    'format': '%(message)s'
                },
            },
        })

    # Extensions

    _extensions = [
        os.path.join(os.path.expanduser('~'), '.run', 'settings.py'),
    ]


settings = Settings()
