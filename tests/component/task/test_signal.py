import unittest
from run.task.signal import TaskSignal, Signal


class TaskSignalTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(TaskSignal, Signal))
