from abc import ABCMeta, abstractmethod


class Module(metaclass=ABCMeta):

    # Public

    @abstractmethod
    def meta_lookup(self, name):
        pass  # pragma: no cover

    @property
    @abstractmethod
    def meta_main_module(self):
        pass  # pragma: no cover

    @property
    @abstractmethod
    def meta_qualname(self):
        pass  # pragma: no cover

    @property
    @abstractmethod
    def meta_tasks(self):
        pass  # pragma: no cover
