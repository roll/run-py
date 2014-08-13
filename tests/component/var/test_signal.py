import unittest
from run.var.signal import VarSignal, TaskSignal


class VarSignalTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(VarSignal, TaskSignal))
