import unittest
from run.module.auto import AutoModule

class AutoModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.module = AutoModule(meta_module=None)

    def test_docstring(self):
        self.assertTrue(self.module)