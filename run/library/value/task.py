from ...task import Task


class ValueTask(Task):

    # Public

    def meta_invoke(self, value):
        return value

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            name='docstring', default='Return value')
