import unittest
from importlib import import_module
from unittest.mock import Mock, patch
component = import_module('run.module.converter')


class module_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.isinstance = patch.object(component, 'isinstance').start()
        self.issubclass = patch.object(component, 'issubclass').start()
        self.module_class = Mock(spec=[])

    # Tests

    @unittest.skip
    def test(self):
        result = component.module(self.module_class)
        self.assertEqual(result, self.module_class.return_value)
        # Check class call
        self.module_class.assert_called_with()

    def test_with_kwargs(self):
        result = component.module(**self.kwargs)(self.module_class)
        self.assertEqual(result, self.module_class.return_value)
        # Check class call
        self.module_class.assert_called_with(**self.kwargs)

