import logging
from box.functools import cachedproperty
from box.importlib import inject
from abc import ABCMeta, abstractmethod

class Resolver(metaclass=ABCMeta):
    """Resolver interface.
    """

    # Public

    @abstractmethod
    def bind(self, attribute):
        """Bind resolver to the attribute.

        :param object attribute: attribute object
        """
        pass  # pragma: no cover

    @abstractmethod
    def enable(self, task_name):
        """Enable resolving for the task.

        :param str task_name: task name
        """
        pass  # pragma: no cover

    @abstractmethod
    def disable(self, task_name):
        """Disable resolving for the task.

        :param str task_name: task name
        """
        pass  # pragma: no cover

    @abstractmethod
    def resolve(self):
        """Resolve itself based on bound attribute.
        """
        pass  # pragma: no cover


class CommonResolver(Resolver):
    """Resolver for the task.

    :param str task_name: task name
    :param tuple args: args to be used in task call
    :param dict kwargs: kwargs to be used in task call
    """

    # Public

    def __init__(self, task_name, *args, **kwargs):
        self._task_name = task_name
        self._args = args
        self._kwargs = kwargs
        self._attribute = None
        self._enabled = True

    def __repr__(self):
        if self._task:
            # TODO: added label if disabled?
            result = str(self._task)
            if self._args or self._kwargs:
                result += '('
                elements = []
                for value in self._args:
                    element = repr(value)
                    elements.append(element)
                for key, value in self._kwargs.items():
                    element = '{0}={1}'.format(str(key), repr(value))
                    elements.append(element)
                result += ', '.join(elements)
                result += ')'
            return result
        else:
            return ('<NotExistent "{task_name}">'.
                format(task_name=self._task_name))

    def bind(self, attribute):
        self._attribute = attribute

    def enable(self, task_name):
        if self._task_name == task_name:
            self._enabled = True

    def disable(self, task_name):
        if self._task_name == task_name:
            self._enabled = False

    def resolve(self):
        if self._enabled:
            if self._task:
                self._task(*self._args, **self._kwargs)

    # Protected

    _getattribute = inject('attribute', module='run.module')
    _task_class = inject('Task', module='run.task')

    @cachedproperty
    def _task(self):
        if self._attribute != None:
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

    def __repr__(self):
        elements = []
        for resolver in self._resolvers:
            elements.append(repr(resolver))
        return repr(elements)

    def bind(self, attribute):
        for resolver in self._resolvers:
            resolver.bind(attribute)

    def enable(self, task_name):
        for resolver in self._resolvers:
            resolver.enable(task_name)

    def disable(self, task_name):
        for resolver in self._resolvers:
            resolver.disable(task_name)

    def resolve(self):
        for resolver in self._resolvers:
            resolver.resolve()
