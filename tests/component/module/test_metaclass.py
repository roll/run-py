import unittest
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
        self.assertIsInstance(self.Class.task_attr, Mock)
        self.assertIsInstance(self.Class.task_builder_attr, MagicMock)
        self.assertEqual(self.Class.abstract_method_attr, self.abstract_method)
        self.assertEqual(self.Class.abstract_descriptor_attr, self.abstract_descriptor)
        self.assertEqual(self.Class.method_attr, 'task')
        self.assertEqual(self.Class.descriptor_attr, 'var')
        self.assertEqual(self.Class.value_attr, 'value_attr')
        self.Metaclass._task.assert_called_with(self.method)
        self.Metaclass._var.assert_called_with(self.descriptor)

    def test___copy__(self):
        # TODO: add more assertions
        self.assertTrue(issubclass(self.Class.__copy__(), self.Class))

    # Protected

    def _make_mock_metaclass(self):
        class MockMetaclass(ModuleMetaclass):
            # Protected
            _task_prototype_class = MagicMock
            _task_class = Mock
            _task = Mock(return_value='task')
            _var = Mock(return_value='var')
        return MockMetaclass

    def _make_mock_class(self, mock_module_metaclass,
        method, descriptor, abstract_method, abstract_descriptor):
        class MockClass(metaclass=mock_module_metaclass):
            # Public
            abstract_method_attr = abstract_method
            abstract_descriptor_attr = abstract_descriptor
            classmethod_attr = classmethod(print)
            descriptor_attr = descriptor
            meta_attr = 'meta_value'
            method_attr = method
            skipped_attr = skip(unittest.TestCase())
            staticmethod_attr = staticmethod(print)
            task_builder_attr = MagicMock()
            task_attr = Mock()
            type_attr = Mock
            UPPER_ATTR = 'upper_attr'
            value_attr = 'value_attr'
            # Protected
            _underscore_attr = 'underscore_value'
        return MockClass
