from ...task import Task


class ProxyTask(Task):

    # Public

    def __init__(self, task, *args, **kwargs):
        self.__task = task
        super().__init__(*args, **kwargs)

    def meta_invoke(self, *args, **kwargs):
        return self.__task_instance(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            'docstring',
            inherit=False,
            default=('Proxy to task "{meta_qualname}".\n{meta_docstring}'.
                     format(meta_qualname=self.__task_instance.meta_qualname,
                            meta_docstring=self.__task_instance.meta_docstring)))

    @property
    def meta_signature(self):
        return self.meta_inspect(
            'signature',
            inherit=False,
            default=self.__task_instance.meta_signature)

    # Private

    @property
    def __task_instance(self):
        return getattr(self.meta_module, self.__task)
