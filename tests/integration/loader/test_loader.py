import os
import unittest
from run.loader import Loader

class ModuleLoaderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.basedir = os.path.join(os.path.dirname(__file__), 'fixtures')
        
    def test_load(self):
        loader = Loader()
        modules = list(loader.load(self.basedir, 'runfile.py', True))
        self.assertEqual(len(modules), 3)
        self.assertEqual(modules[0].__name__, 'Module1')
        self.assertEqual(modules[1].__name__, 'Module2')
        self.assertEqual(modules[2].__name__, 'Module3')
    
    def test_load_with_names(self):
        loader = Loader(names=['name1'])
        modules = list(loader.load(self.basedir, 'runfile.py', True))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module1')

    def test_load_with_tags(self):
        loader = Loader(tags=['tag2'])
        modules = list(loader.load(self.basedir, 'runfile.py', True))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module2')        