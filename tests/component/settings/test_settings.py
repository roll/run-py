import unittest
from run.settings.settings import settings

class SettingsTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(settings)
