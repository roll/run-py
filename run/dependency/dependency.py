import logging
from abc import ABCMeta, abstractmethod
from box.functools import cachedproperty
from ..converter import convert


class Dependency(metaclass=ABCMeta):
    """Dependency representation abstract base class.

    Parameters
    ----------
    predecessor_name: str
        Predecessor name.
    args: tuple
        Args to be used in predecessor call.
    kwargs: dict
        Kwargs to be used in predecessor call.
    """

    # Public

    def __init__(self, predecessor_name, *args, **kwargs):
        self._predecessor_name = predecessor_name
        self._args = args
        self._kwargs = kwargs
        self._enabled = True
        self._successor = None

    def __repr__(self, action=None):
        if action is None:
            action = type(self).__name__
        if self.predecessor is not None:
            predecessor = str(self.predecessor)
            if self._args or self._kwargs:
                predecessor += '('
                elements = []
                for value in self._args:
                    element = repr(value)
                    elements.append(element)
                for key, value in self._kwargs.items():
                    element = '{0}={1}'.format(str(key), repr(value))
                    elements.append(element)
                predecessor += ', '.join(elements)
                predecessor += ')'
        else:
            predecessor = ('<NotExistent "{self._predecessor_name}">'.
                    format(self=self))
        pattern = '{action} {predecessor}'
        if not self._enabled:
            pattern = '{action} {predecessor} [disabled]'
        result = pattern.format(action=action, predecessor=predecessor)
        return result

    def __call__(self, obj):
        converted_object = self._convert(obj)
        converted_object.meta_depend(self)
        return converted_object

    def bind(self, successor):
        """Bind dependency to the successor.

        Parameters
        ----------
        successor: object
            Successor object.
        """
        self._successor = successor

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

        Parameters
        ----------
        failed: bool
            Resolve status.
        """
        pass  # pragma: no cover

    def invoke(self):
        """Invoke predecessor if it exists.
        """
        if self.predecessor is not None:
            self.predecessor(*self._args, **self._kwargs)

    @property
    def enabled(self):
        """Resolving status (enabled or disabled).
        """
        return self._enabled

    @cachedproperty
    def predecessor(self):
        if self._successor is not None:
            try:
                return getattr(
                    self._successor.meta_module, self._predecessor_name)
            except AttributeError as exception:
                if self._successor.meta_strict:
                    raise
                else:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))
                    return None
        else:
            raise RuntimeError(
                'Dependency for "{self._predecessor_name}" '
                'is not bound to any successor'.
                format(self=self))

    @property
    def successor(self):
        return self._successor

    # Protected

    _convert = convert
