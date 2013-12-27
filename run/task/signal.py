from ..attribute import AttributeSignal

class TaskSignal(AttributeSignal): pass
class RequestedTaskSignal(TaskSignal): pass
class CompletedTaskSignal(TaskSignal): pass