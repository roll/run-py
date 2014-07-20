from abc import ABCMeta, abstractmethod
from box.functools import cachedproperty
from .resolver import Resolver, CommonResolver, NestedResolver

class Dependency(Resolver, metaclass=ABCMeta):
    """Dependency representation abstract base class.

    :param str/list task: task name/list of task names/list of dependencies
    :param tuple args: args to be used in task call
    :param dict kwargs: kwargs to be used in task call
    """

    # Public

    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
        self._is_resolved = False

    def __repr__(self):
        return '{category} {resolver}'.format(
            category=type(self).__name__,
            resolver=repr(self._resolver))

    def bind(self, attribute):
        """Bind dependency to the attribute.

        :param object attribute: attribute object
        """
        self._resolver.bind(attribute)

    def enable(self, task):
        """Enable resolving for the task.

        :param str task: task name
        """
        self._resolver.enable(task)

    def disable(self, task):
        """Disable resolving for the task.

        :param str task: task name
        """
        self._resolver.disable(task)

    @abstractmethod
    def resolve(self, failed=None):
        """Resolve itself for bound attribute.
        """
        pass  # pragma: no cover

    @property
    def is_resolved(self):
        """Resolved or not flag.
        """
        return self._is_resolved

    # Protected

    _common_resolver_class = CommonResolver
    _nested_resolver_class = NestedResolver

    @cachedproperty
    def _resolver(self):
        if not isinstance(self._task, list):
            resolver = self._common_resolver_class(
                self._task, *self._args, **self._kwargs)
        else:
            dependencies = []
            for dependency in self._task:
                if not isinstance(dependency, type(self)):
                    dependency = type(self)(
                        dependency, *self._args, **self._kwargs)
                dependencies.append(dependency)
            resolver = self._nested_resolver_class(dependencies)
        return resolver
