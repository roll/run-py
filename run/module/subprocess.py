from box.collections import merge_dicts
from .module import Module
from ..task import SubprocessTask


class SubprocessModule(Module):

    # Public

    def __init__(self, mapping=None, *args,
                 prefix='', separator=' ', **kwargs):
        if mapping is None:
            mapping = {}
        emapping = merge_dicts(self._default_mapping, mapping)
        for task_name, task_prefix in emapping.items():
            if not hasattr(type(self), task_name):
                eprefix = separator.join(filter(None, [prefix, task_prefix]))
                task = SubprocessTask(
                    prefix=eprefix, separator=separator, meta_module=self)
                setattr(type(self), task_name, task)
        super().__init__(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', 'SubprocessModule')

    # Protected

    _default_mapping = {}
