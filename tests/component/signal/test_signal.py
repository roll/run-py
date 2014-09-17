import unittest
from importlib import import_module
component = import_module('run.signal.signal')


class SignalTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(component.Signal, object))