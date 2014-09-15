from abc import ABCMeta, abstractmethod

class Successor(metaclass=ABCMeta):

    # Public

    @property
    @abstractmethod
    def meta_module(self):
        pass  # pragma: no cover

    @property
    @abstractmethod
    def meta_strict(self):
        pass  # pragma: no cover
