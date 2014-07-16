from .module import Module
from ..task import SubprocessTask

class SubprocessModule(Module):

    # Public

    def __init__(self, mapping={}, prefix='', separator=' '):
        emapping = self._default_mapping
        emapping.update(mapping)
        for task_name, task_prefix in emapping.items():
            if not hasattr(type(self), task_name):
                eprefix = separator.join(filter(None, [prefix, task_prefix]))
                task = SubprocessTask(
                    prefix=eprefix, separator=separator, meta_module=self)
                setattr(type(self), task_name, task)

    @property
    def meta_docstring(self):
        return self._meta_params.get('docstring',
            'SubprocessModule')

    # Protected

    _default_mapping = {}
