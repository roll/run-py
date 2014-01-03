import unittest
from run.module.null import NullModule

#Tests

class NullModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.module = MockNullModule(module=None)
        
    def test(self):
        self.assertIsInstance(self.module, MockNullModule)
    
        
#Fixtures

class MockNullModule(NullModule):
    
    #Protected
    
    _meta_default_main_module_name = '__main__'        