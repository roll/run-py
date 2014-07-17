import unittest
from run.task.signal import (InitiatedTaskSignal, SuccessedTaskSignal,
                             FailedTaskSignal, AttributeSignal)

class TaskSignalTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(InitiatedTaskSignal, AttributeSignal))
        self.assertTrue(issubclass(SuccessedTaskSignal, AttributeSignal))
        self.assertTrue(issubclass(FailedTaskSignal, AttributeSignal))
