from ..task import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal

class InitiatedVarSignal(InitiatedTaskSignal): pass
class SuccessedVarSignal(SuccessedTaskSignal): pass
class FailedVarSignal(FailedTaskSignal): pass