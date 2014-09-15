from ..frame.task import Task
from ..frame.var import Var


class AttributeTask(Task):

    # Public

    def __init__(self, attribute, *args, **kwargs):
        self._attribute = attribute
        super().__init__(*args, **kwargs)

    def meta_invoke(self):
        return getattr(self.meta_module, self._attribute)

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', 'Return "{self._attribute}" attribute.'.
            format(self=self))


class AttributeVar(Var, AttributeTask): pass
