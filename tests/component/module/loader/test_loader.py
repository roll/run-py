import os
import unittest
from run import ModuleLoader

class ModuleLoaderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.loader = ModuleLoader()
        self.path = os.path.join(os.path.dirname(__file__), 'fixtures')
        
    def test_load(self):
        modules = list(self.loader.load(self.path, 'runfile.py', True))
        self.assertEqual(len(modules), 2)
        self.assertEqual(modules[0].__name__, 'Module1')
        self.assertEqual(modules[1].__name__, 'Module2')