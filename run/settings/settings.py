from box.logging import Settings
from ..version import version


class Settings(Settings):

    # Main

    cache = True
    compact = False
    convert = True
    fallback = None
    filename = 'runfile.py'
    inherit = ['meta_*']
    plain = False
    strict = True
    workdir = None

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
        return self._inherit_argparse(Settings, {
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


settings = Settings()
