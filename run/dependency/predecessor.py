from abc import ABCMeta, abstractmethod

class Predecessor(metaclass=ABCMeta):

    # Public

    @abstractmethod
    def __call__(self):
        pass  # pragma: no cover
