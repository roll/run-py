from ...task import Task


class ValueTask(Task):

    # Public

    def meta_invoke(self, value):
        return value

    @property
    def meta_docstring(self):
        return self._meta_get_parameter(
            'docstring', inherit=False, default='Return value')
