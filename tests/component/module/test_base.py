import unittest
from unittest.mock import Mock
from run.module.base import BaseModule

#Tests

class BaseModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.module = MockBaseModule(module=None)
    
    def test(self):
        self.assertIsInstance(self.module, MockBaseModule)
    
    def test___get__(self):
        self.assertIs(self.module.__get__(None), self.module)
        
    def test___set__(self):
        self.assertRaises(AttributeError, self.module.__set__, None, 'value')

    def test___getattr__(self):
        self.assertEqual(getattr(self.module, '__getattr__.__doc__'), None)
        self.assertRaises(AttributeError, getattr, self.module, 'no_attr')

    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, '__main__')
    
    def test_meta_main_module(self):
        self.assertIs(self.module.meta_main_module, self.module)
    
    def test_meta_is_main_module(self):
        self.assertTrue(self.module.meta_is_main_module)
        
    def test_meta_tags(self):
        self.assertEqual(self.module.meta_tags, [])
        
    def test_meta_attributes(self):
        self.assertEqual(len(self.module.meta_attributes), 1)                  
        
        
class ModuleTest_with_module_is_main(BaseModuleTest):

    #Public
    
    def setUp(self):
        self.main_module = MockMainModule()
        self.module = MockBaseModule(module=self.main_module)
        self.main_module.meta_attributes = {'module': self.module}
        
    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, 'module')
        
    def test_meta_main_module(self):
        self.assertIs(self.module.meta_main_module, self.main_module)    
        
    def test_meta_is_main_module(self):
        self.assertFalse(self.module.meta_is_main_module)                      
    
    
#Fixtures

class MockBaseModule(BaseModule):

    #Public

    attr1 = 'value1'
    meta_dispatcher = Mock(add_signal=Mock())
    meta_basedir = None
    
    #Protected
    
    _meta_default_main_module_name = '__main__'
    
    
class MockMainModule:

    #Public
    
    meta_name = 'main_module'
    meta_is_main_module = True
    meta_attributes = {}
    
    @property
    def meta_main_module(self):
        return self    