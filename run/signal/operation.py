from abc import ABCMeta, abstractmethod
from box.terminal import Formatter
from ..settings import settings
from .signal import Signal


class OperationSignal(Signal):

    # Public

    def __init__(self, *, operation, event):
        self._operation = operation
        self._event = event

    def format(self):
        result = self._events.get(self.event, '')
        if result:
            if not self.operation.meta_plain:
                style = self._styles.get(self.event, None)
                if style is not None:
                    formater = Formatter()
                    result = formater.format(result, **style)
        return result

    @property
    def operation(self):
        return self._operation

    @property
    def event(self):
        return self._event

    # Protected

    _events = settings.events
    _styles = settings.styles


class Operation(metaclass=ABCMeta):

    # Public

    @abstractmethod
    def meta_format(self, mode=None):
        pass  # pragma: no cover

    @property
    @abstractmethod
    def meta_module(self):
        pass  # pragma: no cover

