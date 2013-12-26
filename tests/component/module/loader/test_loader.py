import os
import unittest
from run import ModuleLoader

class ModuleLoaderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.loader = ModuleLoader()
        self.base_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        
    def test_load(self):
        objects = list(self.loader.load(
            self.base_dir, 'runfile.py', recursively=True))
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0].__name__, 'Module1')
        self.assertEqual(objects[1].__name__, 'Module2')