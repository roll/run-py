from abc import ABCMeta, abstractmethod

class Container(metaclass=ABCMeta):

    # Public

    @property
    @abstractmethod
    def meta_basedir(self):
        pass  # pragma: no cover
