import unittest
from unittest.mock import Mock
from run.module.null import NullModule

#Tests

class NullModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.module = MockNullModule(module=None)
        
    def test(self):
        self.assertIsInstance(self.module, MockNullModule)
        
    def test_meta_module(self):
        self.assertEqual(self.module.meta_module, self.module)
        
    def test_meta_module_setter(self):
        self.assertRaises(AttributeError, 
            setattr, self.module, 'meta_module', 'module')        
        
    def test_meta_is_bound(self):
        self.assertEqual(self.module.meta_is_bound, False)
        
    def test_meta_dispatcher(self):
        self.assertEqual(self.module.meta_dispatcher, 'dispatcher')
        
    def test_meta_basedir(self):
        self.assertEqual(self.module.meta_basedir, 'default_path')
        
    def test_meta_qualname(self):
        self.assertEqual(self.module.meta_qualname, '__main__')                                         
    
        
#Fixtures

class MockNullModule(NullModule):
    
    #Protected
    
    _meta_default_main_module_name = '__main__'
    _meta_dispatcher_class = Mock(return_value='dispatcher')  
    _meta_default_path = 'default_path'   