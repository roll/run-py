import unittest
from abc import abstractmethod
from unittest.mock import Mock, MagicMock
from run.module.metaclass import ModuleMetaclass

class ModuleMetaclassTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.function = lambda: None
        self.descriptor = property(lambda: None)
        self.abstract_function = abstractmethod(lambda: None)
        self.abstract_descriptor = property(abstractmethod(lambda: None))
        self.MockModuleMetaclass = self._make_mock_module_metaclass()
        self.MockModule = self._make_mock_module_class(
            self.MockModuleMetaclass,
            function = self.function,
            descriptor = self.descriptor,
            abstract_function = self.abstract_function,
            abstract_descriptor = self.abstract_descriptor)

    def test___new__(self):
        self.assertEqual(self.MockModule.__name__, 'MockModule')
        self.assertEqual(self.MockModule.__bases__, (object,))
        self.assertEqual(self.MockModule._underscore_attr, 'underscore_value')
        self.assertEqual(self.MockModule.meta_attr, 'meta_value')
        self.assertEqual(self.MockModule.type_attr, Mock)
        self.assertIsInstance(self.MockModule.attribute_attr, Mock)
        self.assertIsInstance(self.MockModule.attribute_builder_attr, MagicMock)
        self.assertEqual(self.MockModule.abstract_function_attr, self.abstract_function)
        self.assertEqual(self.MockModule.abstract_descriptor_attr, self.abstract_descriptor)
        self.assertEqual(self.MockModule.function_attr, 'function_task_attr')
        self.assertEqual(self.MockModule.descriptor_attr, 'descriptor_var_attr')
        self.assertEqual(self.MockModule.value_attr, 'value_var_attr')
        self.MockModuleMetaclass._function_task_class.assert_called_with(self.function)
        self.MockModuleMetaclass._descriptor_var_class.assert_called_with(self.descriptor)
        self.MockModuleMetaclass._value_var_class.assert_called_with('value_attr')
        
    #Protected
    
    def _make_mock_module_metaclass(self):
        class MockModuleMetaclass(ModuleMetaclass):
            #Public
            _attribute_class = Mock
            _attribute_builder_class = MagicMock
            _function_task_class = Mock(return_value='function_task_attr')
            _descriptor_var_class = Mock(return_value='descriptor_var_attr')
            _value_var_class = Mock(return_value='value_var_attr')
        return MockModuleMetaclass
    
    def _make_mock_module_class(self, mock_module_metaclass, 
        function, descriptor, abstract_function, abstract_descriptor):
        class MockModule(metaclass=mock_module_metaclass):
            #Public
            _underscore_attr = 'underscore_value'
            meta_attr = 'meta_value'
            type_attr = Mock
            attribute_attr = Mock()
            attribute_builder_attr = MagicMock()
            abstract_function_attr = abstract_function
            abstract_descriptor_attr = abstract_descriptor
            function_attr = function
            descriptor_attr = descriptor
            value_attr = 'value_attr'
        return MockModule