import re
from .function import FunctionTask


class MethodTask(FunctionTask):

    # Public

    def __init__(self, method, *args, **kwargs):
        super().__init__(method, *args, **kwargs)

    @property
    def meta_signature(self):
        return self._meta_params.get(
            'signature', re.sub('self[,\s]*', '', super().meta_signature))

    def meta_invoke(self, *args, **kwargs):
        return self._function(self.meta_module, *args, **kwargs)
