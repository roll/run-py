from abc import ABCMeta, abstractmethod

class Module(metaclass=ABCMeta):

    # Public

    @property
    @abstractmethod
    def meta_basedir(self):
        pass  # pragma: no cover
