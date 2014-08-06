import unittest
from unittest.mock import Mock
from run.module.find import FindModule

class FindModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.inner_module = Mock()

    def test___new__(self):
        Module = self._make_MockModule(self.inner_module)
        module = Module(
            names='names',
            tags='tags',
            file='file',
            basedir='basedir',
            recursively='recursively')
        self.assertIsInstance(module, Mock)
        Module._find.assert_called_with(
            names='names',
            tags='tags',
            file='file',
            basedir='basedir',
            recursively='recursively',
            getfirst=True)

    def test___new___no_modules(self):
        Module = self._make_MockModule()
        self.assertRaises(Exception, Module)

    # Protected

    def _make_MockModule(self, module=None):
        class MockModule(FindModule):
            # Protected
            _find = Mock(return_value=module)
        return MockModule
