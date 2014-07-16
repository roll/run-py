from abc import ABCMeta, abstractmethod
from box.dependency import inject
from ..attribute import AttributePrototype

class DependencyDecorator(metaclass=ABCMeta):

    # Public

    def __call__(self, method):
        prototype = method
        if not isinstance(method, AttributePrototype):
            prototype = self._method_task_class(method)
        self._add_dependency(prototype)
        return prototype

    # Protected

    _method_task_class = inject('MethodTask', module='run.task')

    @abstractmethod
    def _add_dependency(self, prototype):
        pass  # pragma: no cover
