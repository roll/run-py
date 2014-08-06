import unittest
from run.task.signal import (InitiatedTaskSignal, SuccessedTaskSignal,
                             FailedTaskSignal, Signal)


class TaskSignalTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(InitiatedTaskSignal, Signal))
        self.assertTrue(issubclass(SuccessedTaskSignal, Signal))
        self.assertTrue(issubclass(FailedTaskSignal, Signal))
