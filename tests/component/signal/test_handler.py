import inspect
import unittest
from importlib import import_module
component = import_module('run.signal.handler')


class HandlerTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(component.Handler, object))
        self.assertTrue(inspect.isabstract(component.Handler))
