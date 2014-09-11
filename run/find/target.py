from abc import ABCMeta, abstractmethod


class Target(metaclass=ABCMeta):

    # Public

    @property
    @abstractmethod
    def meta_key(self):
        pass  # pragma: no cover

    @property
    @abstractmethod
    def meta_tags(self):
        pass  # pragma: no cover
