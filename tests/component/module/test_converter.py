import unittest
from unittest.mock import Mock, patch
from run.module import converter


class module_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.isinstance = patch.object(converter, 'isinstance').start()
        self.issubclass = patch.object(converter, 'issubclass').start()
        self.module_class = Mock(spec=[])

    def test(self):
        result = converter.module(self.module_class)
        self.assertEqual(result, self.module_class.return_value)
        # Check class call
        self.module_class.assert_called_with()

    def test_with_kwargs(self):
        result = converter.module(**self.kwargs)(self.module_class)
        self.assertEqual(result, self.module_class.return_value)
        # Check class call
        self.module_class.assert_called_with(**self.kwargs)

