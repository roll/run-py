import unittest
from unittest.mock import Mock
from run.module.module_function import module

class module_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.module = module()

    def test_expand(self):
        mock_module = Mock()
        mock_attr2 = getattr(mock_module, 'attr1.attr2')
        self.module.attr1.attr2(*self.args, **self.kwargs)
        self.assertEqual(
            self.module.expand(mock_module),
            mock_attr2.return_value)
        # Check attribute call
        mock_attr2.assert_called_with(*self.args, **self.kwargs)
