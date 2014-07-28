import unittest
from unittest.mock import Mock
from run.attribute.update import AttributeSet, AttributeCall

class AttributeSetTest(unittest.TestCase):

    # Public

    def test_apply(self):
        update = AttributeSet('name', 'value')
        obj = Mock()
        update.apply(obj)
        self.assertEqual(obj.name, 'value')


class AttributeCallTest(unittest.TestCase):

    # Public

    def test_apply(self):
        update = AttributeCall('method', 'value')
        obj = Mock(method=Mock())
        update.apply(obj)
        obj.method.assert_called_with('value')
