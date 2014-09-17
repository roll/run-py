from ...task import Task


class NullTask(Task):

    # Public

    def meta_invoke(self):
        pass

    @property
    def meta_docstring(self):
        return self.meta_params.get(
            'docstring', 'Do nothing but resolve dependencies.')
