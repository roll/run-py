from abc import ABCMeta
from ..task import Task


class Var(Task, metaclass=ABCMeta):

    # Public

    @property
    def meta_is_descriptor(self):
        return True

    @property
    def meta_signature(self):
        return ''

    @property
    def meta_style(self):
        # TODO: move default to settings?
        return self.meta_get_parameter(
            'style', inherit=False, default='var')

    @meta_style.setter
    def meta_style(self, value):
        self.meta_set_parameter('style', value)
