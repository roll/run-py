import unittest
from importlib import import_module
component = import_module('run.settings')


class SettingsTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(component.settings)
