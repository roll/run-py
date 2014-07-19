import logging
from box.functools import cachedproperty
from box.importlib import inject
from abc import ABCMeta, abstractmethod

class Resolver(metaclass=ABCMeta):
    """Resolver representation abstract base class.
    """

    # Public

    def __init__(self):
        self._attribute = None

    def bind(self, attribute):
        """Bind resolver to attribute.

        :param object attribute: attribute object
        """
        self._attribute = attribute

    @abstractmethod
    def enable(self, task):
        """Enable resolving for task.

        :param str task: task name
        """
        pass  # pragma: no cover

    @abstractmethod
    def disable(self, task):
        """Disable resolving for task.

        :param str task: task name
        """
        pass  # pragma: no cover

    @abstractmethod
    def resolve(self):
        """Resolve itself for bound attribute.
        """
        pass  # pragma: no cover


class CommonResolver(Resolver):
    """Resolver for concrete task.

    :param str task: task name
    :param tuple args: args to be used in task call
    :param dict kwargs: kwargs to be used in task call
    """

    # Public

    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        self._args = args
        self._kwargs = kwargs
        self._enabled = True
        super().__init__()

    def __repr__(self):
        if self._task:
            result = repr(self._task)
            if self._args or self._kwargs:
                result += '('
                elements = []
                for arg in self._args:
                    element = repr(arg)
                    elements.append(element)
                for kwarg in self._kwargs.items():
                    element = '{0}={1}'.format(*kwarg)
                    elements.append(element)
                result += ', '.join(elements)
                result += ')'
            return result
        else:
            return ('<NotExistent "{task_name}">'.
                format(task_name=self._task_name))

    def enable(self, task):
        if task == self._task:
            self._enabled = True

    def disable(self, task):
        if task == self._task:
            self._enabled = False

    def resolve(self):
        if self._task:
            self._task(*self._args, **self._kwargs)

    # Protected

    _getattribute = inject('attribute', module='run.module')
    _task_class = inject('Task', module='run.task')

    @cachedproperty
    def _task(self):
        if self._attribute:
            module = self._attribute.meta_module
            try:
                return self._getattribute(module, self._task_name,
                    category=self._task_class, getvalue=True)
            except AttributeError as exception:
                if self._attribute.meta_strict:
                    raise
                else:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))
                    return None
        else:
            raise RuntimeError(
                'Dependency resolver for "{task_name}" '
                'is not bound to any attribute'.
                format(task_name=self._task_name))


class NestedResolver(Resolver):
    """Resolver for group of nested resolvers.

    :param list resolvers: nested resolvers
    """

    # Public

    def __init__(self, resolvers):
        self._resolvers = resolvers
        super().__init__()

    def __repr__(self):
        elements = []
        for resolver in self._resolvers:
            elements.append(repr(resolver))
        return repr(elements)

    def bind(self, attribute):
        for resolver in self._resolvers:
            resolver.bind(attribute)

    def enable(self, task):
        for resolver in self._resolvers:
            resolver.enable(task)

    def disable(self, task):
        for resolver in self._resolvers:
            resolver.disable(task)

    def resolve(self):
        for resolver in self._resolvers:
            resolver.resolve()
