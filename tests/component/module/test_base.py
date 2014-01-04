import os
import inspect
import unittest
from run.module.base import BaseModule

class BaseModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.MockBaseModule = self._make_mock_base_module_class()
        self.module = self.MockBaseModule(module=None)
    
    def test(self):
        self.assertIsInstance(self.module, self.MockBaseModule)
    
    def test___get__(self):
        self.assertIs(self.module.__get__(None), self.module)
        
    def test___set__(self):
        self.assertRaises(AttributeError, self.module.__set__, None, 'value')

    def test___getattr__(self):
        self.assertEqual(getattr(self.module, '__getattr__.__doc__'), None)
        self.assertRaises(AttributeError, getattr, self.module, 'no_attr')
        
    def test_meta_attributes(self):
        self.assertEqual(len(self.module.meta_attributes), 1)  
    
    def test_meta_basedir(self):
        self.assertEqual(self.module.meta_basedir, 
                         os.path.dirname(inspect.getfile(type(self))))
        
    def test_meta_dispatcher(self):
        self.assertEqual(self.module.meta_dispatcher, 
                         self.module.meta_module.meta_dispatcher)
    
    def test_meta_docstring(self):
        self.assertEqual(self.module.meta_docstring, 'docstring')
        
    def test_meta_info(self):
        self.assertEqual(self.module.meta_info, 
                         '__main__'+'\n'+'docstring') 
        
    def test_meta_is_bound(self):
        self.assertEqual(self.module.meta_is_bound, False)               
        
    def test_meta_is_main_module(self):
        self.assertTrue(self.module.meta_is_main_module)
    
    def test_meta_main_module(self):
        self.assertIs(self.module.meta_main_module, self.module)
   
    def test_meta_module(self):
        #Null module
        self.assertNotEqual(self.module.meta_module, None)
        self.assertFalse(self.module.meta_module)
        
    def test_meta_module_setter(self):
        self.module.meta_module = 'module'
        self.assertEqual(self.module.meta_module, 'module')         
            
    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, '__main__')
        
    def test_meta_qualname(self):
        self.assertEqual(self.module.meta_qualname, '__main__')        
        
    def test_meta_signature(self):
        self.assertEqual(self.module.meta_signature, '__main__')
        
    def test_meta_tags(self):
        self.assertEqual(self.module.meta_tags, [])
        
    def test_meta_type(self):
        self.assertEqual(self.module.meta_type, 'MockBaseModuleBuilded')
        
    #Protected
    
    def _make_mock_base_module_class(self):
        class MockBaseModule(BaseModule):
            """docstring"""
            #Public
            attr1 = 'value1'
            #Protected
            _meta_default_main_module_name = '__main__'
        return MockBaseModule      
        
        
class ModuleTest_with_module_is_main(BaseModuleTest):

    #Public
    
    def setUp(self):
        self.MockBaseModule = self._make_mock_base_module_class()
        MockMainModule = self._make_mock_main_module_class()
        self.main_module = MockMainModule()
        self.module = self.MockBaseModule(module=self.main_module)
        self.main_module.meta_attributes = {'module': self.module}
    
    def test_meta_info(self):
        self.assertEqual(self.module.meta_info, 
                         '[main_module] module'+'\n'+'docstring') 
        
    def test_meta_is_bound(self):
        self.assertEqual(self.module.meta_is_bound, True)        
        
    def test_meta_is_main_module(self):
        self.assertFalse(self.module.meta_is_main_module)  
        
    def test_meta_main_module(self):
        self.assertIs(self.module.meta_main_module, self.main_module)  
   
    def test_meta_module(self):
        self.assertEqual(self.module.meta_module, self.main_module)
        
    def test_meta_module_setter(self):
        self.assertRaises(AttributeError, 
            setattr, self.module, 'meta_module', 'module')          
           
    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, 'module')
        
    def test_meta_qualname(self):
        self.assertEqual(self.module.meta_qualname, '[main_module] module')         
        
    def test_meta_signature(self):
        self.assertEqual(self.module.meta_signature, '[main_module] module') 
        
    #Protected
    
    def _make_mock_main_module_class(self):
        class MockMainModule:
            #Public
            meta_attributes = {}
            meta_dispatcher = 'dispatcher'
            meta_is_main_module = True
            meta_name = 'main_module'
            meta_qualname = 'main_module'    
            @property
            def meta_main_module(self):
                return self
        return MockMainModule 