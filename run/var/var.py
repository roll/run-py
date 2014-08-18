from abc import ABCMeta
from ..task import Task


class Var(Task, metaclass=ABCMeta):

    # Public

    def __get__(self, module, module_class=None):
        return self()

    @property
    def meta_signature(self):
        return ''

    # Protected

    _meta_style = 'var'  # Overriding
