import os
import unittest
from run import ModuleLoader

class ModuleLoaderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.loader = ModuleLoader()
        self.path = os.path.join(os.path.dirname(__file__), 'fixtures')
        
    def test_load(self):
        objects = list(self.loader.load(self.path, 'runfile.py', True))
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0].__name__, 'Module1')
        self.assertEqual(objects[1].__name__, 'Module2')