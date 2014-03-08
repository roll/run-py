import unittest
from abc import abstractmethod
from unittest.mock import Mock, MagicMock
from run.module.metaclass import ModuleMetaclass

class ModuleMetaclassTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.method = lambda self: None
        self.descriptor = property(lambda self: None)
        self.abstract_method = abstractmethod(lambda self: None)
        self.abstract_descriptor = property(abstractmethod(lambda self: None))
        self.MockModuleMetaclass = self._make_mock_module_metaclass()
        self.MockModule = self._make_mock_module_class(
            self.MockModuleMetaclass,
            method = self.method,
            descriptor = self.descriptor,
            abstract_method = self.abstract_method,
            abstract_descriptor = self.abstract_descriptor)

    def test___new__(self):
        self.assertEqual(self.MockModule.__name__, 'MockModule')
        self.assertEqual(self.MockModule.__bases__, (object,))
        self.assertEqual(self.MockModule._underscore_attr, 'underscore_value')
        self.assertEqual(self.MockModule.meta_attr, 'meta_value')
        self.assertEqual(self.MockModule.type_attr, Mock)
        self.assertIsInstance(self.MockModule.attribute_attr, Mock)
        self.assertIsInstance(self.MockModule.attribute_builder_attr, MagicMock)
        self.assertEqual(self.MockModule.abstract_method_attr, self.abstract_method)
        self.assertEqual(self.MockModule.abstract_descriptor_attr, self.abstract_descriptor)
        self.assertEqual(self.MockModule.method_attr, 'method_task_attr')
        self.assertEqual(self.MockModule.descriptor_attr, 'descriptor_var_attr')
        self.assertEqual(self.MockModule.value_attr, 'value_var_attr')
        self.MockModuleMetaclass._method_task_class.assert_called_with(self.method)
        self.MockModuleMetaclass._descriptor_var_class.assert_called_with(self.descriptor)
        self.MockModuleMetaclass._value_var_class.assert_called_with('value_attr')
        
    #Protected
    
    def _make_mock_module_metaclass(self):
        class MockModuleMetaclass(ModuleMetaclass):
            #Public
            _attribute_class = Mock
            _attribute_draft_class = MagicMock
            _method_task_class = Mock(return_value='method_task_attr')
            _descriptor_var_class = Mock(return_value='descriptor_var_attr')
            _value_var_class = Mock(return_value='value_var_attr')
        return MockModuleMetaclass
    
    def _make_mock_module_class(self, mock_module_metaclass, 
        method, descriptor, abstract_method, abstract_descriptor):
        class MockModule(metaclass=mock_module_metaclass):
            #Public
            _underscore_attr = 'underscore_value'
            meta_attr = 'meta_value'
            type_attr = Mock
            attribute_attr = Mock()
            attribute_builder_attr = MagicMock()
            abstract_method_attr = abstract_method
            abstract_descriptor_attr = abstract_descriptor
            method_attr = method
            descriptor_attr = descriptor
            value_attr = 'value_attr'
        return MockModule