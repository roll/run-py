import unittest
from unittest.mock import Mock
from run.module.attribute import attribute

class attribute_Test(unittest.TestCase):

    # Public

    def test(self):
        module = Mock(__getattribute__=Mock(return_value='gotten_attribute'))
        gotten_attribute = attribute(module,
            'name', category='category', getvalue='getvalue')
        self.assertEqual(gotten_attribute, 'gotten_attribute')
        module.__getattribute__.assert_called_with(
            'name', category='category', getvalue='getvalue')
