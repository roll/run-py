import unittest
from abc import abstractmethod
from unittest.mock import Mock, MagicMock
from run.module.metaclass import ModuleMetaclass

#Tests

class ModuleMetaclassTest(unittest.TestCase):

    #Public

    def test___new__(self):
        self.assertEqual(MockModule.__name__, 'MockModule')
        self.assertEqual(MockModule.__bases__, (object,))
        self.assertEqual(MockModule._underscore_attr, 'underscore_value')
        self.assertEqual(MockModule.meta_attr, 'meta_value')
        self.assertEqual(MockModule.type_attr, Mock)
        self.assertIsInstance(MockModule.attribute_attr, Mock)
        self.assertIsInstance(MockModule.attribute_builder_attr, MagicMock)
        self.assertEqual(MockModule.abstract_method_attr, abstract_method)
        self.assertEqual(MockModule.abstract_property_attr, abstract_property)
        self.assertEqual(MockModule.method_attr, 'method_task_attr')
        self.assertEqual(MockModule.property_attr, 'property_var_attr')
        self.assertEqual(MockModule.value_attr, 'value_var_attr')
        MockModuleMetaclass._method_task_class.assert_called_with(method)
        MockModuleMetaclass._property_var_class.assert_called_with(prop)
        MockModuleMetaclass._value_var_class.assert_called_with('value_attr')
    
    
#Fixtures

method = lambda: None
prop = property(lambda: None)
abstract_method = abstractmethod(lambda: None)
abstract_property = property(abstractmethod(lambda: None))

class MockModuleMetaclass(ModuleMetaclass):

    #Public

    _attribute_class = Mock
    _attribute_builder_class = MagicMock
    _method_task_class = Mock(return_value='method_task_attr')
    _property_var_class = Mock(return_value='property_var_attr')
    _value_var_class = Mock(return_value='value_var_attr')
    
    
class MockModule(metaclass=MockModuleMetaclass):
    
    #Public
    
    _underscore_attr = 'underscore_value'
    meta_attr = 'meta_value'
    type_attr = Mock
    attribute_attr = Mock()
    attribute_builder_attr = MagicMock()
    abstract_method_attr = abstract_method
    abstract_property_attr = abstract_property
    method_attr = method
    property_attr = prop
    value_attr = 'value_attr'