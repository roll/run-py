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
    
    def test_meta_attributes(self):
        self.assertEqual(self.module.meta_attributes, {})
        
    def test_meta_basedir(self):
        self.assertEqual(self.module.meta_basedir, 'default_basedir')
        
    def test_meta_dispatcher(self):
        self.assertEqual(self.module.meta_dispatcher, 'null_dispatcher')
        
    def test_meta_docstring(self):
        self.assertEqual(self.module.meta_docstring, 'docstring')        
        
    def test_meta_info(self):
        self.assertEqual(self.module.meta_info, '__main__'+'\n'+'docstring')
           
    def test_meta_is_bound(self):
        self.assertEqual(self.module.meta_is_bound, False)
           
    def test_meta_is_main_module(self):
        self.assertEqual(self.module.meta_is_main_module, True)
           
    def test_meta_main_module(self):
        self.assertEqual(self.module.meta_main_module, self.module)
               
    def test_meta_module(self):
        self.assertEqual(self.module.meta_module, self.module)
        
    def test_meta_module_setter(self):
        self.assertRaises(AttributeError, 
            setattr, self.module, 'meta_module', 'module')  
    
    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, '__main__') 
              
    def test_meta_qualname(self):
        self.assertEqual(self.module.meta_qualname, '__main__')
              
    def test_meta_signature(self):
        self.assertEqual(self.module.meta_signature, '__main__')
              
    def test_meta_tags(self):
        self.assertEqual(self.module.meta_tags, [])
              
    def test_meta_type(self):
        self.assertEqual(self.module.meta_type, 'MockNullModuleBuilded')                                                 
    
        
#Fixtures

class MockNullModule(NullModule):
    """docstring"""
    
    #Protected
    
    _meta_default_main_module_name = '__main__'
    _meta_null_dispatcher_class = Mock(return_value='null_dispatcher')  
    _meta_default_basedir = 'default_basedir'   