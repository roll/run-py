from abc import ABCMeta, abstractmethod
from ..helpers import cachedproperty, pack
from .convert import convert


class Dependency(metaclass=ABCMeta):
    """Dependency representation abstract base class.

    Parameters
    ----------
    target: str
        Dependency target relative to module.
    args: tuple
        Args to be used in predecessor call.
    kwargs: dict
        Kwargs to be used in predecessor call.
    """

    # Public

    def __init__(self, __target, *args, **kwargs):
        self.__target = __target
        self.__args = args
        self.__kwargs = kwargs
        self.__successor = None

    def __repr__(self, action=None):
        if action is None:
            action = type(self).__name__
        if self.predecessor is not None:
            predecessor = str(self.predecessor)
            predecessor += pack(*self.__args, **self.__kwargs)
        else:
            template = '<NotExistent "{target}">'
            predecessor = template.format(target=self.__target)
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
    def resolve(self, fail=None):
        """Resolve dependency.

        Parameters
        ----------
        fail: bool
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
            return getattr(self.__successor.meta_module, self.__target)
        raise RuntimeError(
            'Dependency for "{target}" is not bound'.
            format(target=self.__target))

    @property
    def successor(self):
        return self.__successor
