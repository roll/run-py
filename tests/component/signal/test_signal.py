import unittest
from run.signal.signal import Signal


class SignalTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(Signal, object))