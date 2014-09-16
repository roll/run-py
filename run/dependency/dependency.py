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

    # TODO: namespaces collision?
    def __init__(self, predecessor_name, *args, **kwargs):
        self.__predecessor_name = predecessor_name
        self.__args = args
        self.__kwargs = kwargs
        self.__successor = None

    def __repr__(self, action=None):
        if action is None:
            action = type(self).__name__
        if self.predecessor is not None:
            predecessor = str(self.predecessor)
            if self.__args or self.__kwargs:
                predecessor += '('
                elements = []
                for value in self.__args:
                    element = repr(value)
                    elements.append(element)
                for key, value in self.__kwargs.items():
                    element = '{0}={1}'.format(str(key), repr(value))
                    elements.append(element)
                predecessor += ', '.join(elements)
                predecessor += ')'
        else:
            predecessor = ('<NotExistent "{predecessor_name}">'.
                format(predecessor_name=self.__predecessor_name))
        pattern = '{action} {predecessor}'
        result = pattern.format(action=action, predecessor=predecessor)
        return result

    def __call__(self, obj):
        converted_object = convert(obj)
        converted_object.meta_depend(self)
        return converted_object

    def bind(self, successor):
        """Bind dependency to the successor.

        Parameters
        ----------
        successor: object
            Successor object.
        """
        self.__successor = successor

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
            self.predecessor(*self.__args, **self.__kwargs)

    @cachedproperty
    def predecessor(self):
        if self.__successor is not None:
            try:
                return getattr(
                    self.__successor.meta_module, self.__predecessor_name)
            except AttributeError as exception:
                if self.__successor.meta_strict:
                    raise
                else:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))
                    return None
        else:
            raise RuntimeError(
                'Dependency for "{predecessor_name}" '
                'is not bound to any successor'.
                format(predecessor_name=self.__predecessor_name))

    @property
    def successor(self):
        return self.__successor
