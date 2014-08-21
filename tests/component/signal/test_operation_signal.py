import unittest
from run.signal.operation import OperationSignal, Signal


class TaskSignalTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(OperationSignal, Signal))
