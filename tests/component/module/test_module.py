import unittest
from unittest.mock import Mock, call
from run.module.module import Module

class ModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.MockModule = self._make_mock_module_class()
        self.module = self.MockModule(meta_module=None)              
    
    def test(self):
        self.assertIsInstance(self.module, self.MockModule)
    
    def test___get__(self):
        self.assertIs(self.module.__get__(None), self.module)
        
    def test___set__(self):
        self.assertRaises(AttributeError, self.module.__set__, None, 'value')
        
    def test___getattr___no_attribute(self):
        self.assertRaises(AttributeError, getattr, self.module, 'no_attr')
        self.assertRaises(AttributeError, getattr, self.module, 'no_attr.req')      
        
    def test_meta_attributes(self):
        self.assertEqual(len(self.module.meta_attributes), 5)  
    
    def test_meta_basedir(self):
        self.assertEqual(self.module.meta_basedir, 
                         self.module.meta_module.meta_basedir)
        
    def test_meta_dispatcher(self):
        self.assertEqual(self.module.meta_dispatcher, 
                         self.module.meta_module.meta_dispatcher)
    
    def test_meta_docstring(self):
        self.assertEqual(self.module.meta_docstring, 'docstring')
        
    def test_meta_info(self):
        self.assertEqual(self.module.meta_info, 
                         '__main__'+'\n'+'docstring') 
        
    def test_meta_is_main_module(self):
        self.assertTrue(self.module.meta_is_main_module)
    
    def test_meta_main_module(self):
        self.assertIs(self.module.meta_main_module, self.module)
   
    def test_meta_module(self):
        #Null module
        self.assertNotEqual(self.module.meta_module, None)
        self.assertFalse(self.module.meta_module)
            
    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, '__main__')
        
    def test_meta_qualname(self):
        self.assertEqual(self.module.meta_qualname, '__main__')        
        
    def test_meta_signature(self):
        self.assertEqual(self.module.meta_signature, '__main__')
        
    def test_meta_tags(self):
        self.assertEqual(self.module.meta_tags, [])
        
    def test_meta_type(self):
        self.assertEqual(self.module.meta_type, 'MockModule')
        
    def test_list(self):
        self.module.list()
        self.module._print_function.assert_has_calls([
            call('attr1'), 
            call('default'), 
            call('info'), 
            call('list'), 
            call('meta')])
    
    def test_info(self):
        self.module.info()  
        self.module._print_function.assert_called_with(
            '__main__'+'\n'+'docstring')
    
    def test_meta(self):
        self.module.meta()           
        self.assertTrue(self.module._pprint_function.called)
        
    #Protected
    
    def _make_mock_module_class(self):
        class MockModule(Module):
            """docstring"""            
            #Public
            attr1 = 'value1'
            #Protected
            _meta_default_main_module_name = '__main__'
            _print_function = Mock()            
            _pprint_function = Mock()
        return MockModule
        
        
class ModuleTest_with_module_is_main(ModuleTest):

    #Public
    
    def setUp(self):
        self.MockModule = self._make_mock_module_class()
        self.MockMainModule = self._make_mock_main_module_class()
        self.main_module = self.MockMainModule()
        self.module = self.MockModule(meta_module=self.main_module)
        self.main_module.meta_attributes = {'module': self.module}
    
    def test_meta_info(self):
        self.assertEqual(self.module.meta_info, 
                         '[main_module] module'+'\n'+'docstring')      
        
    def test_meta_is_main_module(self):
        self.assertFalse(self.module.meta_is_main_module)  
        
    def test_meta_main_module(self):
        self.assertIs(self.module.meta_main_module, self.main_module)  
   
    def test_meta_module(self):
        self.assertEqual(self.module.meta_module, self.main_module)         
           
    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, 'module')
        
    def test_meta_qualname(self):
        self.assertEqual(self.module.meta_qualname, '[main_module] module')         
        
    def test_meta_signature(self):
        self.assertEqual(self.module.meta_signature, '[main_module] module')
         
    def test_list(self):
        self.module.list()
        self.module._print_function.assert_has_calls([
            call('[main_module] module.attr1'), 
            call('[main_module] module.default'), 
            call('[main_module] module.info'), 
            call('[main_module] module.list'), 
            call('[main_module] module.meta')])        
        
    def test_info(self):
        self.module.info()  
        (self.module._print_function.
            assert_called_with('[main_module] module'+'\n'+'docstring'))                        
    
    #Protected
    
    def _make_mock_main_module_class(self):
        class MockMainModule:
            #Public
            meta_attributes = {}   
            meta_basedir = '.'
            meta_cache = True
            meta_fallback = None
            meta_dispatcher = Mock(add_signal=Mock())
            meta_is_main_module = True
            meta_name = 'main_module'
            meta_qualname = 'main_module'    
            @property
            def meta_main_module(self):
                return self
        return MockMainModule 