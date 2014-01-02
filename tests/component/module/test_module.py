import unittest
from unittest.mock import Mock, call
from run.module.module import Module

#Tests

class ModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.module = MockModule(module=None)
    
    def test(self):
        self.assertIsInstance(self.module, MockModule)
    
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
        self.assertEqual(len(self.module.meta_attributes), 5)                  
    
    def test_list(self):
        self.module._meta_print_operator.reset_mock()
        self.module.list()
        self.module._meta_print_operator.assert_has_calls([
            call('attr1'), 
            call('default'), 
            call('info'), 
            call('list'), 
            call('meta')])
    
    def test_info(self):
        self.module._meta_print_operator.reset_mock()
        self.module.info()  
        self.module._meta_print_operator.assert_called_with('__main__')
    
    def test_meta(self):
        self.module._meta_print_operator.reset_mock()
        self.module.meta()           
        self.assertTrue(self.module._meta_formatted_print_operator.called)
        
        
class ModuleTest_with_module_is_main(ModuleTest):

    #Public
    
    def setUp(self):
        self.main_module = MockMainModule()
        self.module = MockModule(module=self.main_module)
        self.main_module.meta_attributes = {'module': self.module}
        
    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, 'module')
        
    def test_meta_main_module(self):
        self.assertIs(self.module.meta_main_module, self.main_module)    
        
    def test_meta_is_main_module(self):
        self.assertFalse(self.module.meta_is_main_module) 
        
    def test_list(self):
        self.module._meta_print_operator.reset_mock()
        self.module.list()
        self.module._meta_print_operator.assert_has_calls([
            call('[main_module] module.attr1'), 
            call('[main_module] module.default'), 
            call('[main_module] module.info'), 
            call('[main_module] module.list'), 
            call('[main_module] module.meta')])        
        
    def test_info(self):
        self.module._meta_print_operator.reset_mock()
        self.module.info()  
        (self.module._meta_print_operator.
            assert_called_with('[main_module] module'))                        
    
    
#Fixtures

class MockModule(Module):

    #Public

    attr1 = 'value1'
    meta_dispatcher = Mock(add_signal=Mock())
    meta_basedir = None
    
    #Protected
    
    _meta_default_main_module_name = '__main__'
    _meta_formatted_print_operator = Mock()
    _meta_print_operator = Mock()
    
    
class MockMainModule:

    #Public
    
    meta_name = 'main_module'
    meta_is_main_module = True
    meta_attributes = {}
    
    @property
    def meta_main_module(self):
        return self    