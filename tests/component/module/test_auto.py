import unittest
import fractions
from run.module.auto import AutoModule

class AutoModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.module = AutoModule([fractions], meta_module=None)
    
    def test_meta_attributes(self):
        self.assertEqual(sorted(self.module.meta_attributes), 
            ['default', 'gcd', 'info', 'list', 'meta'])
        
    def test_meta_docstring(self):
        self.assertTrue(self.module.meta_docstring)
        
    def test_gcd(self):
        self.assertEqual(self.module.gcd(10, 15), 5)        