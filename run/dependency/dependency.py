import logging
from abc import ABCMeta, abstractmethod
from box.functools import cachedproperty
from box.importlib import inject

class Dependency(metaclass=ABCMeta):
    """Dependency representation abstract base class.

    :param task: task name
    :param tuple args: args to be used in task call
    :param dict kwargs: kwargs to be used in task call
    """

    # Public

    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
        self._enabled = True
        self._successor = None

    def __repr__(self, action=None):
        if action == None:
            action = type(self).__name__
        if self.predecessor != None:
            # TODO: added label if not enabled?
            task = str(self.predecessor)
            if self._args or self._kwargs:
                task += '('
                elements = []
                for value in self._args:
                    element = repr(value)
                    elements.append(element)
                for key, value in self._kwargs.items():
                    element = '{0}={1}'.format(str(key), repr(value))
                    elements.append(element)
                task += ', '.join(elements)
                task += ')'
        else:
            task = '<NotExistent "{self.task}">'.format(self=self)
        result = '{action} {task}'.format(action=action, task=task)
        return result

    def __call__(self, method):
        prototype = method
        # TODO: moved this logic to task.task()?
        if not isinstance(method, self._task_prototype_class):
            prototype = self._task_function(method)
        prototype.meta_depend(self)
        return prototype

    def bind(self, task):
        """Bind dependency to the task.

        :param object task: task object
        """
        self._successor = task

    def enable(self):
        """Enable resolving.
        """
        self._enabled = True

    def disable(self):
        """Disable resolving.
        """
        self._enabled = False

    @abstractmethod
    def resolve(self, failed=None):
        """Resolve dependency.

        :param bool failed: resolve status
        """
        pass  # pragma: no cover

    def invoke(self):
        """Invoke task if it exists.
        """
        if self.predecessor != None:
            self.predecessor(*self._args, **self._kwargs)

    @property
    def task(self):
        """Dependency's task name.
        """
        return self._task

    @property
    def enabled(self):
        """Resolving status (enabled or disabled).
        """
        return self._enabled

    @cachedproperty
    def predecessor(self):
        if self._successor != None:
            module = self._successor.meta_module
            try:
                task = getattr(module, self._task)
                return task
            except AttributeError as exception:
                if self._successor.meta_strict:
                    raise
                else:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))
                    return None
        else:
            raise RuntimeError(
                'Dependency for "{self.task}" '
                'is not bound to any task'.
                format(self=self))

    @property
    def successor(self):
        return self._successor

    # Protected

    _task_function = inject('task', module='run.task')
    _task_prototype_class = inject('TaskPrototype', module='run.task')
