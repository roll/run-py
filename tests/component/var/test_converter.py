import unittest
from unittest.mock import patch
from importlib import import_module
component = import_module('run.var.converter')


class var_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.property = patch('builtins.property').start()
        self.isfunction = patch('inspect.isfunction').start()
        self.DescriptorVar = patch.object(component, 'DescriptorVar').start()

    # Tests

    def test(self):
        result = component.var('method')
        self.assertEqual(result, self.DescriptorVar.return_value)
        # Check property call
        self.property.assert_called_with('method')
        # Check DescriptorVar call
        self.DescriptorVar.assert_called_with(self.property.return_value)

    def test_with_kwargs(self):
        result = component.var(**self.kwargs)('method')
        self.assertEqual(result, self.DescriptorVar.return_value)
        # Check property call
        self.property.assert_called_with('method')
        # Check DescriptorVar call
        self.DescriptorVar.assert_called_with(
            self.property.return_value, **self.kwargs)
