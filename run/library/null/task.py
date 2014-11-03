from ...task import Task


class NullTask(Task):

    # Public

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            name='docstring', lookup=True,
            default='Do nothing but resolve dependencies.')

    def meta_invoke(self):
        pass
