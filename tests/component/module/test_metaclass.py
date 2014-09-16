import unittest
from unittest.mock import Mock, patch
from run.module import metaclass


class ModuleMetaclassTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.fork = Mock()
        self.convert = Mock()
        patch.object(metaclass, 'TaskPrototype', Mock).start()
        patch.object(metaclass, 'fork', self.fork).start()
        patch.object(metaclass, 'convert', self.convert).start()
        self.Class = self._make_mock_class()

    def test___meta_spawn__(self):
        result = self.Class.__meta_spawn__()
        self.assertTrue(issubclass(result, self.Class))
        self.assertEqual(result.__name__, 'MockClass')
        self.assertEqual(result.__bases__, (self.Class,))
        self.assertEqual(result.UPPER_ATTR, 'UPPER_ATTR')
        self.assertEqual(result._underscore_attr, '_underscore_attr')
        self.assertEqual(result.meta_attr, 'meta_attr')
        self.assertEqual(result.prototype, self.fork.return_value)
        self.assertEqual(result.task, self.convert.return_value)
        # Check fork call
        self.fork.assert_called_with(self.Class.prototype)
        # Check convert call
        self.convert.assert_called_with('task')

    # Protected

    def _make_mock_class(self):
        class MockClass(metaclass=metaclass.ModuleMetaclass):
            # Public
            meta_convert = True
            UPPER_ATTR = 'UPPER_ATTR'
            _underscore_attr = '_underscore_attr'
            meta_attr = 'meta_attr'
            prototype = Mock()
            task = 'task'
        return MockClass
