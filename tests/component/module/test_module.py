import unittest
from unittest.mock import Mock, call
from run.module.module import Module

class ModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockModule = self._make_mock_module_class()
        self.module = MockModule(module=None)              
    
    def test_list(self):
        self.module.list()
        self.module._meta_print_function.assert_has_calls([
            call('attr1'), 
            call('default'), 
            call('info'), 
            call('list'), 
            call('meta')])
    
    def test_info(self):
        self.module.info()  
        self.module._meta_print_function.assert_called_with('__main__')
    
    def test_meta(self):
        self.module.meta()           
        self.assertTrue(self.module._meta_pprint_function.called)
        
    #Protected
    
    def _make_mock_module_class(self):
        class MockModule(Module):
            #Public
            attr1 = 'value1'
            #Protected
            _meta_default_main_module_name = '__main__'
            _meta_pprint_function = Mock()
            _meta_print_function = Mock()
        return MockModule
        
        
class ModuleTest_with_module_is_main(ModuleTest):

    #Public
    
    def setUp(self):
        MockModule = self._make_mock_module_class()
        MockMainModule = self._make_mock_main_module_class()
        self.main_module = MockMainModule()
        self.module = MockModule(module=self.main_module)
        self.main_module.meta_attributes = {'module': self.module}
        
    def test_list(self):
        self.module.list()
        self.module._meta_print_function.assert_has_calls([
            call('[main_module] module.attr1'), 
            call('[main_module] module.default'), 
            call('[main_module] module.info'), 
            call('[main_module] module.list'), 
            call('[main_module] module.meta')])        
        
    def test_info(self):
        self.module.info()  
        (self.module._meta_print_function.
            assert_called_with('[main_module] module'))                        
    
    #Protected
    
    def _make_mock_main_module_class(self):
        class MockMainModule:
            #Public
            meta_attributes = {}    
            meta_dispatcher = Mock(add_signal=Mock())
            meta_is_main_module = True
            meta_name = 'main_module'
            meta_qualname = 'main_module'    
            @property
            def meta_main_module(self):
                return self
        return MockMainModule 