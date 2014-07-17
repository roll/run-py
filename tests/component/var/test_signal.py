import unittest
from run.var.signal import (InitiatedVarSignal, InitiatedTaskSignal,
                            SuccessedVarSignal, SuccessedTaskSignal,
                            FailedVarSignal, FailedTaskSignal)

class DerivedVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(InitiatedVarSignal, InitiatedTaskSignal))
        self.assertTrue(issubclass(SuccessedVarSignal, SuccessedTaskSignal))
        self.assertTrue(issubclass(FailedVarSignal, FailedTaskSignal))
