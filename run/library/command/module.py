from box.collections import merge_dicts
from ...module import Module
from .task import CommandTask


class CommandModule(Module):

    # Public

    def __init__(self, mapping=None, *args, **kwargs):
        if mapping is None:
            mapping = {}
        emapping = merge_dicts(self._default_mapping, mapping)
        for name, command in emapping.items():
            if not hasattr(type(self), name):
                task = CommandTask(command, meta_module=self)
                setattr(type(self), name, task)
        super().__init__(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self.meta_params.get(
            'docstring', 'CommandModule')

    # Protected

    _default_mapping = {}
