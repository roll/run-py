from ...task import Task


class ClusterTask(Task):

    # Public

    def __init__(self, tasks, *args, **kwargs):
        self.__tasks = tasks
        super().__init__(*args, **kwargs)

    def meta_invoke(self, *args, **kwargs):
        results = []
        for task in self.__tasks:
            result = task(*args, **kwargs)
            results.append(result)
        return results

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            name='docstring', lookup=True,
            default='Invoke "{tasks}" tasks.'.format(tasks=self.__tasks))
