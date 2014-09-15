import unittest
from run.frame.signal.signal import Signal


class SignalTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(Signal, object))