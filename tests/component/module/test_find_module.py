import unittest
from unittest.mock import Mock
from run.module.find_module import FindModule


class FindModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.inner_module = Mock()

    @unittest.skip('not fixed after reimplementing')
    def test___new__(self):
        Module = self._make_mock_module_class(self.inner_module)
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

    @unittest.skip('not fixed after reimplementing')
    def test___new___no_modules(self):
        Module = self._make_mock_module_class()
        self.assertRaises(Exception, Module)

    # Protected

    def _make_mock_module_class(self, module=None):
        class MockModule(FindModule):
            # Protected
            _find = Mock(return_value=module)
        return MockModule
