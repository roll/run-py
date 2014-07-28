from ..task import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal

class InitiatedModuleSignal(InitiatedTaskSignal): pass
class SuccessedModuleSignal(SuccessedTaskSignal): pass
class FailedModuleSignal(FailedTaskSignal): pass
