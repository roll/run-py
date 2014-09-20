from ...task import Task


class NullTask(Task):

    # Public

    def meta_invoke(self):
        pass

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            name='docstring', default='Do nothing but resolve dependencies.')
