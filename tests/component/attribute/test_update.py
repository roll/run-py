import unittest
from unittest.mock import Mock
from run.attribute.update import AttributeBuilderSet, AttributeBuilderCall

#Tests

class AttributeBuilderSetTest(unittest.TestCase):

    #Public

    def test_apply(self):
        update = AttributeBuilderSet('name', 'value')
        obj = Mock()
        update.apply(obj)
        self.assertEqual(obj.name, 'value')
      

class AttributeBuilderCallTest(unittest.TestCase):

    #Public

    def test_apply(self):
        update = AttributeBuilderCall('method', 'value')
        obj = Mock(method=Mock())
        update.apply(obj)
        obj.method.assert_called_with('value')