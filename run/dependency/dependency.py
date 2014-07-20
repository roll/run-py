import logging
from abc import ABCMeta, abstractmethod
from box.functools import cachedproperty
from box.importlib import inject
from ..attribute import AttributePrototype

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
        self._attribute = None
        self._enabled = True

    def __repr__(self, action=None):
        if action == None:
            action = type(self).__name__
        if self._task_instance:
            # TODO: added label if not enabled?
            task = str(self._task_instance)
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
            task = '<NotExistent "{self.task_name}">'.format(self=self)
        result = '{action} {task}'.format(action=action, task=task)
        return result

    def __call__(self, method):
        prototype = method
        if not isinstance(method, AttributePrototype):
            prototype = self._method_task_class(method)
        prototype.depend(self)
        return prototype

    def bind(self, attribute):
        """Bind dependency to the attribute.

        :param object attribute: attribute object
        """
        self._attribute = attribute

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
        if self._task_instance:
            self._task_instance(*self._args, **self._kwargs)

    @property
    def attribute(self):
        """Dependency's attribute (if bound or None).
        """
        return self._attribute

    @property
    def enabled(self):
        """Resolving status (enabled or disabled).
        """
        return self._enabled

    @property
    def task(self):
        """Dependency's task name.
        """
        return self._task

    # Protected

    _getattribute = inject('attribute', module='run.module')
    _method_task_class = inject('MethodTask', module='run.task')
    _task_class = inject('Task', module='run.task')

    @cachedproperty
    def _task_instance(self):
        if self._attribute != None:
            module = self._attribute.meta_module
            try:
                task = self._getattribute(module, self._task,
                    category=self._task_class, getvalue=True)
                return task
            except AttributeError as exception:
                if self._attribute.meta_strict:
                    raise
                else:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))
                    return None
        else:
            raise RuntimeError(
                'Dependency for "{self.task}" '
                'is not bound to any attribute'.
                format(self=self))
