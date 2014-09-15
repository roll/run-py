import unittest
from unittest.mock import Mock
from run.module.prototype import ModulePrototype


# TODO: implement
class ModulePrototypeTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Module = self._make_mock_module_class()
        self.Prototype = self._make_mock_prototype_class()
        self.prototype = self.Prototype(self.Module, None)

    # Protected

    def _make_mock_module_class(self):
        class MockModule:
            # Public
            attr = 'attr'
            task = Mock(__meta_init__=Mock(return_value='task'))
            @classmethod
            def __meta_fork__(cls):
                return cls
        return MockModule

    def _make_mock_prototype_class(self):
        class MockPrototype(ModulePrototype):
            # Protected
            _TaskPrototype = Mock
        return MockPrototype
