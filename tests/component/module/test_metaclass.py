import unittest
from copy import copy
from abc import abstractmethod
from unittest.mock import Mock, MagicMock
from run.module.metaclass import ModuleMetaclass

class ModuleMetaclassTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.method = lambda self: None
        self.descriptor = property(lambda self: None)
        self.abstract_method = abstractmethod(lambda self: None)
        self.abstract_descriptor = property(abstractmethod(lambda self: None))
        self.MockMetaclass = self._make_mock_metaclass()
        self.MockClass = self._make_mock_class(
            self.MockMetaclass,
            method=self.method,
            descriptor=self.descriptor,
            abstract_method=self.abstract_method,
            abstract_descriptor=self.abstract_descriptor)

    def test___new__(self):
        self.assertEqual(self.MockClass.__name__, 'MockClass')
        self.assertEqual(self.MockClass.__bases__, (object,))
        self.assertEqual(self.MockClass._underscore_attr, 'underscore_value')
        self.assertEqual(self.MockClass.meta_attr, 'meta_value')
        self.assertEqual(self.MockClass.type_attr, Mock)
        self.assertIsInstance(self.MockClass.attribute_attr, Mock)
        self.assertIsInstance(self.MockClass.attribute_builder_attr, MagicMock)
        self.assertEqual(self.MockClass.abstract_method_attr, self.abstract_method)
        self.assertEqual(self.MockClass.abstract_descriptor_attr, self.abstract_descriptor)
        self.assertEqual(self.MockClass.method_attr, 'method_task_attr')
        self.assertEqual(self.MockClass.descriptor_attr, 'descriptor_var_attr')
        self.assertEqual(self.MockClass.value_attr, 'value_var_attr')
        self.MockMetaclass._method_task_class.assert_called_with(self.method)
        self.MockMetaclass._descriptor_var_class.assert_called_with(self.descriptor)
        self.MockMetaclass._value_var_class.assert_called_with('value_attr')

    def test___copy__(self):
        self.assertTrue(issubclass(copy(self.MockClass), self.MockClass))

    # Protected

    def _make_mock_metaclass(self):
        class MockMetaclass(ModuleMetaclass):
            # Protected
            _attribute_class = Mock
            _attribute_prototype_class = MagicMock
            _method_task_class = Mock(return_value='method_task_attr')
            _descriptor_var_class = Mock(return_value='descriptor_var_attr')
            _value_var_class = Mock(return_value='value_var_attr')
        return MockMetaclass

    def _make_mock_class(self, mock_module_metaclass,
        method, descriptor, abstract_method, abstract_descriptor):
        class MockClass(metaclass=mock_module_metaclass):
            # Public
            meta_attr = 'meta_value'
            type_attr = Mock
            attribute_attr = Mock()
            attribute_builder_attr = MagicMock()
            abstract_method_attr = abstract_method
            abstract_descriptor_attr = abstract_descriptor
            method_attr = method
            descriptor_attr = descriptor
            value_attr = 'value_attr'
            # Protected
            _underscore_attr = 'underscore_value'
        return MockClass
