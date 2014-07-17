import unittest
from copy import copy
from abc import abstractmethod
from unittest.mock import Mock, MagicMock
from run.module.metaclass import ModuleMetaclass, skip

class ModuleMetaclassTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.method = lambda self: None
        self.descriptor = property(lambda self: None)
        self.abstract_method = abstractmethod(lambda self: None)
        self.abstract_descriptor = property(abstractmethod(lambda self: None))
        self.Metaclass = self._make_mock_metaclass()
        self.Class = self._make_mock_class(
            self.Metaclass,
            method=self.method,
            descriptor=self.descriptor,
            abstract_method=self.abstract_method,
            abstract_descriptor=self.abstract_descriptor)

    def test___new__(self):
        self.assertEqual(self.Class.__name__, 'MockClass')
        self.assertEqual(self.Class.__bases__, (object,))
        self.assertEqual(self.Class._underscore_attr, 'underscore_value')
        self.assertEqual(self.Class.meta_attr, 'meta_value')
        self.assertEqual(self.Class.type_attr, Mock)
        self.assertIsInstance(self.Class.attribute_attr, Mock)
        self.assertIsInstance(self.Class.attribute_builder_attr, MagicMock)
        self.assertEqual(self.Class.abstract_method_attr, self.abstract_method)
        self.assertEqual(self.Class.abstract_descriptor_attr, self.abstract_descriptor)
        self.assertEqual(self.Class.method_attr, 'method_task_attr')
        self.assertEqual(self.Class.descriptor_attr, 'descriptor_var_attr')
        self.assertEqual(self.Class.value_attr, 'value_var_attr')
        self.Metaclass._method_task_class.assert_called_with(self.method)
        self.Metaclass._descriptor_var_class.assert_called_with(self.descriptor)
        self.Metaclass._value_var_class.assert_called_with('value_attr')

    def test___copy__(self):
        self.assertTrue(issubclass(copy(self.Class), self.Class))

    # Protected

    def _make_mock_metaclass(self):
        class MockMetaclass(ModuleMetaclass):
            # Protected
            _attribute_class = Mock
            _attribute_prototype_class = MagicMock
            _descriptor_var_class = Mock(return_value='descriptor_var_attr')
            _method_task_class = Mock(return_value='method_task_attr')
            _value_var_class = Mock(return_value='value_var_attr')
        return MockMetaclass

    def _make_mock_class(self, mock_module_metaclass,
        method, descriptor, abstract_method, abstract_descriptor):
        class MockClass(metaclass=mock_module_metaclass):
            # Public
            attribute_attr = Mock()
            attribute_builder_attr = MagicMock()
            abstract_method_attr = abstract_method
            abstract_descriptor_attr = abstract_descriptor
            classmethod_attr = classmethod(print)
            descriptor_attr = descriptor
            meta_attr = 'meta_value'
            method_attr = method
            skipped_attr = skip(unittest.TestCase())
            staticmethod_attr = staticmethod(print)
            type_attr = Mock
            value_attr = 'value_attr'
            UPPER_ATTR = 'upper_attr'
            # Protected
            _underscore_attr = 'underscore_value'
        return MockClass
