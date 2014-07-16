import unittest
from unittest.mock import Mock
from run.attribute.build import build

class build_Test(unittest.TestCase):
    
    #Public
    
    def test(self):
        prototype = Mock(__build__=Mock(return_value='attribute'))
        attribute = build(prototype, 'module')
        self.assertEqual(attribute, 'attribute')
        prototype.__build__.assert_called_with('module')