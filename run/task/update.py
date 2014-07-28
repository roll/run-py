class TaskUpdate:

    # Public

    def __init__(self, name, *args, **kwargs):
        self._name = name
        self._args = args
        self._kwargs = kwargs

    def apply(self, attribute):
        method = getattr(attribute, self._name)
        method(*self._args, **self._kwargs)
