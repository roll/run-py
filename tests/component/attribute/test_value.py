import unittest
from unittest.mock import Mock
from run.attribute.value import value

class value_Test(unittest.TestCase):

    # Public

    def test(self):
        attribute = Mock(__get__=Mock(return_value='attribute_value'))
        attribute_value = value(attribute)
        self.assertEqual(attribute_value, 'attribute_value')
        attribute.__get__.assert_called_with(attribute.meta_module)
