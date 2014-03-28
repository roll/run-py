import unittest
from unittest.mock import Mock
from run.module.draft import ModuleDraft

class ModuleDraftTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockModuleDraft = self._make_mock_module_draft_class()
        self.MockModule = self._make_mock_module_class()
        self.draft = MockModuleDraft(self.MockModule)
    
    def test__create_object(self):
        obj = self.draft._create_object()
        self.assertIsInstance(obj, self.draft._builded_class)
        
    def test__builded_class(self):
        self.assertTrue(issubclass(self.draft._builded_class, 
                                   self.MockModule))
        
    def test__builded_class_name(self):
        self.assertEqual(
            self.draft._builded_class_name, 
                         'MockModuleBuilded')    
     
    def test__builded_class_bases(self):
        self.assertEqual(self.draft._builded_class_bases, 
                         (self.MockModule,))
        
    def test__builded_class_attrs(self):
        self.assertEqual(self.draft._builded_class_attrs, {
            '__doc__': 'docstring',
            '__module__': type(self).__module__,
            'attr1': 'value1',
            'attr2': 'value2',
        })
    
    #Protected
    
    def _make_mock_module_class(self):
        class BaseMockModule:
            #Public
            __on_created__ = lambda *args, **kwargs: None
            attr1 = Mock(meta_draft=Mock(return_value='value1'))
        class MockModule(BaseMockModule):
            """docstring"""
            #Public
            attr2 = Mock(meta_draft=Mock(return_value='value2'))
        return MockModule
    
    def _make_mock_module_draft_class(self):    
        class MockModuleDraft(ModuleDraft):
            #Protected
            _attribute_draft_class = Mock
        return MockModuleDraft