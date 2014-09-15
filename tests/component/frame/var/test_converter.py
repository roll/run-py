import unittest
from unittest.mock import patch
from run.frame.var import converter


class var_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.property = patch('builtins.property').start()
        self.isfunction = patch('inspect.isfunction').start()
        self.DescriptorVar = patch.object(converter, 'DescriptorVar').start()

    def test(self):
        result = converter.var('method')
        self.assertEqual(result, self.DescriptorVar.return_value)
        # Check property call
        self.property.assert_called_with('method')
        # Check DescriptorVar call
        self.DescriptorVar.assert_called_with(self.property.return_value)

    def test_with_kwargs(self):
        result = converter.var(**self.kwargs)('method')
        self.assertEqual(result, self.DescriptorVar.return_value)
        # Check property call
        self.property.assert_called_with('method')
        # Check DescriptorVar call
        self.DescriptorVar.assert_called_with(
            self.property.return_value, **self.kwargs)
