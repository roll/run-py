from ...task import Task


class NullTask(Task):

    # Public

    def meta_invoke(self):
        pass

    @property
    def meta_docstring(self):
        return self._meta_get_parameter(
            'docstring',
            inherit=False,
            default='Do nothing but resolve dependencies.')
