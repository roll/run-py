from abc import ABCMeta
from ..task import Task


class Var(Task, metaclass=ABCMeta):

    # Public

    def __get__(self, module, module_class=None):
        return self()

    @property
    def meta_signature(self):
        return ''

    @property
    def meta_style(self):
        return 'var'
