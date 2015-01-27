import unittest
from importlib import import_module
component = import_module('run.helpers.settings')


class SettingsTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.Settings = self.make_mock_settings_class()
        self.settings = self.Settings()

    # Helpers

    def make_mock_settings_class(self):
        class MockSettings(component.Settings):
            # Public
            name1 = 'value1'
        return MockSettings

    # Tests

    def test(self):
        self.assertEqual(self.settings, {'name1': 'value1'})

    def test_upper(self):
        self.settings = self.Settings(upper=True)
        self.assertEqual(self.settings, {'NAME1': 'value1'})

    def test___setattr__(self):
        self.settings.name2 = 'value2'
        self.assertEqual(self.settings, {'name1': 'value1', 'name2': 'value2'})

    def test___delattr__(self):
        self.settings.name2 = 'value2'
        del self.settings.name2
        self.assertEqual(self.settings, {'name1': 'value1'})
