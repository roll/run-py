from ...task import Task


class AttributeTask(Task):

    # Public

    def __init__(self, attribute, *args, **kwargs):
        self.__attribute = attribute
        super().__init__(*args, **kwargs)

    def meta_invoke(self):
        return getattr(self.meta_module, self.__attribute)

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', 'Return "{attribute}" attribute.'.
            format(attribute=self.__attribute))
