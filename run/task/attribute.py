from .task import Task

class AttributeTask(Task):

    # Public

    @property
    def meta_docstring(self):
        return self._meta_params.get('docstring',
            'Return "{self.attribute}" attribute.'.format(self=self))

    def invoke(self, attribute):
        return getattr(self.meta_module, attribute)