import unittest
from unittest.mock import Mock
from run.module.metaclass import ModuleMetaclass


class ModuleMetaclassTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Metaclass = self._make_mock_metaclass()
        self.Class = self._make_mock_class(self.Metaclass)

    def test___spawn__(self):
        result = self.Class.__spawn__()
        self.assertTrue(issubclass(result, self.Class))
        self.assertEqual(result.__name__, 'MockClass')
        self.assertEqual(result.__bases__, (self.Class,))
        self.assertEqual(result.UPPER_ATTR, 'UPPER_ATTR')
        self.assertEqual(result._underscore_attr, '_underscore_attr')
        self.assertEqual(result.meta_attr, 'meta_attr')
        self.assertEqual(result.prototype, self.Metaclass._fork.return_value)
        self.assertEqual(result.task, self.Metaclass._convert.return_value)
        # Check fork call
        self.Metaclass._fork.assert_called_with(self.Class.prototype)
        # Check convert call
        self.Metaclass._convert.assert_called_with('task')

    # Protected

    def _make_mock_metaclass(self):
        class MockMetaclass(ModuleMetaclass):
            # Protected
            _convert = Mock()
            _default_convert = True
            _fork = Mock()
            _BaseTaskPrototype = Mock
        return MockMetaclass

    def _make_mock_class(self, metaclass):
        class MockClass(metaclass=metaclass):
            # Public
            UPPER_ATTR = 'UPPER_ATTR'
            _underscore_attr = '_underscore_attr'
            meta_attr = 'meta_attr'
            prototype = Mock()
            task = 'task'
        return MockClass
