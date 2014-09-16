class TaskUpdate:

    # Public

    def __init__(self, name, *args, **kwargs):
        self.__name = name
        self.__args = args
        self.__kwargs = kwargs

    def apply(self, task):
        method = getattr(task, self.__name)
        method(*self.__args, **self.__kwargs)
