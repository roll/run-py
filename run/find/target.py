from abc import ABCMeta, abstractmethod

class Target(metaclass=ABCMeta):

    # Public

    @property
    @abstractmethod
    def meta_name(self):
        pass  # pragma: no cover

    @property
    @abstractmethod
    def meta_tags(self):
        pass  # pragma: no cover
