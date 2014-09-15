import unittest
from run.frame.signal.null import NullDispatcher


class NullDispatcherTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.dispatcher = NullDispatcher()

    def test___bool__(self):
        self.assertFalse(self.dispatcher)
