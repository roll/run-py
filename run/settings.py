from .helpers import Settings


class Settings(Settings):

    # Main

    cache = True
    chdir = True
    fallback = None
    filename = 'runfile.py'
    plain = False

    # Converters

    converters = [
        # Short 'run.module' doesn't work
        # in shell for nosetests
        'run.module.module',
        'run.task.task',
        'run.var.var',
    ]

    # Listeners

    listeners = [
        'run.Logger',
    ]

    # Styles

    styles = {
        'init': {'foreground': 'bright_yellow'},
        'fail': {'foreground': 'bright_red'},
        'done': {'foreground': 'bright_green'},
        'module': {'foreground': 'bright_cyan'},
        'task': {'foreground': 'bright_blue'},
        'var': {'foreground': 'bright_magenta'},
    }

    # Logging

    logging_level = 'INFO'
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
