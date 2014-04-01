import unittest
from unittest.mock import Mock
from run.module.prototype import ModulePrototype

class ModulePrototypeTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.MockPrototype = self._make_mock_prototype_class()
        self.MockModule = self._make_mock_module_class()
        self.prototype = self.MockPrototype(self.MockModule, None)
    
    def test__create_attribute(self):
        module = self.prototype._create_attribute()
        self.assertIsInstance(module, self.MockModule)
        self.assertEqual(module.attr, 'value')
    
    #Protected
    
    def _make_mock_module_class(self):
        class MockModule:
            #Public
            attr = Mock(return_value='value')
        return MockModule
    
    def _make_mock_prototype_class(self):    
        class MockPrototype(ModulePrototype):
            #Protected
            _attribute_prototype_class = Mock
        return MockPrototype