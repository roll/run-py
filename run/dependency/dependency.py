from abc import ABCMeta, abstractmethod
from sugarbowl import cachedproperty
from ..converter import convert


class Dependency(metaclass=ABCMeta):
    """Dependency representation abstract base class.

    Parameters
    ----------
    predecessor_name: str
        Predecessor name.
    """

    # Public

    def __init__(self, predecessor_name):
        self.__predecessor_name = predecessor_name
        self.__successor = None

    def __repr__(self, action=None):
        if action is None:
            action = type(self).__name__
        if self.predecessor is not None:
            predecessor = str(self.predecessor)
        else:
            predecessor = ('<NotExistent "{predecessor_name}">'.
                format(predecessor_name=self.__predecessor_name))
        template = '{action} {predecessor}'
        result = template.format(action=action, predecessor=predecessor)
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
            self.predecessor()

    @cachedproperty
    def predecessor(self):
        if self.__successor is not None:
            return getattr(
                self.__successor.meta_module,
                self.__predecessor_name)
        raise RuntimeError(
            'Dependency for "{predecessor_name}" is not bound'.
            format(predecessor_name=self.__predecessor_name))

    @property
    def successor(self):
        return self.__successor
