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
        self.assertEqual(MockModule.abstract_function_attr, abstract_function)
        self.assertEqual(MockModule.abstract_descriptor_attr, abstract_descriptor)
        self.assertEqual(MockModule.function_attr, 'function_task_attr')
        self.assertEqual(MockModule.descriptor_attr, 'descriptor_var_attr')
        self.assertEqual(MockModule.value_attr, 'value_var_attr')
        MockModuleMetaclass._function_task_class.assert_called_with(function)
        MockModuleMetaclass._descriptor_var_class.assert_called_with(descriptor)
        MockModuleMetaclass._value_var_class.assert_called_with('value_attr')
    
    
#Fixtures

function = lambda: None
descriptor = property(lambda: None)
abstract_function = abstractmethod(lambda: None)
abstract_descriptor = property(abstractmethod(lambda: None))

class MockModuleMetaclass(ModuleMetaclass):

    #Public

    _attribute_class = Mock
    _attribute_builder_class = MagicMock
    _function_task_class = Mock(return_value='function_task_attr')
    _descriptor_var_class = Mock(return_value='descriptor_var_attr')
    _value_var_class = Mock(return_value='value_var_attr')
    
    
class MockModule(metaclass=MockModuleMetaclass):
    
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