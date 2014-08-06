import unittest
from unittest.mock import Mock
from run.module.prototype import ModulePrototype

class ModulePrototypeTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Module = self._make_mock_module_class()
        self.Prototype = self._make_mock_prototype_class()
        self.prototype = self.Prototype(self.Module, None)

    @unittest.skip('not changed to _initiate_task')
    def test__initiate_task(self):
        self.module = self.prototype._create_task()
        self.assertIsInstance(self.module, self.Module)
        self.assertEqual(self.Module.attr, 'attr')
        self.assertEqual(self.Module.task, 'task')

    # Protected

    def _make_mock_module_class(self):
        class MockModule:
            # Public
            attr = 'attr'
            task = Mock(__initiate__=Mock(return_value='task'))
            @classmethod
            def __fork__(cls):
                return cls
        return MockModule

    def _make_mock_prototype_class(self):
        class MockPrototype(ModulePrototype):
            # Protected
            _TaskPrototype = Mock
        return MockPrototype
