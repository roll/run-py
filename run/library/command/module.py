from ...module import Module
from .task import CommandTask


class CommandModule(Module):

    # Public

    def __init__(self, mapping, *args, **kwargs):
        for name, command in mapping.items():
            if not hasattr(type(self), name):
                task = CommandTask(command, meta_module=self)
                setattr(type(self), name, task)
        super().__init__(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self.meta_get_parameter(
            'docstring', inherit=False, default='CommandModule')
