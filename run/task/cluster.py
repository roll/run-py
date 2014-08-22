from .task import Task


class ClusterTask(Task):

    # Public

    def __init__(self, tasks, *args, **kwargs):
        self._tasks = tasks
        super().__init__(*args, **kwargs)

    def meta_invoke(self, *args, **kwargs):
        results = []
        for task in self._tasks:
            result = task(*args, **kwargs)
            results.append(result)
        return results

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', 'Invoke "{self._tasks}" tasks.'.format(self=self))
