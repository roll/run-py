import unittest
from unittest.mock import Mock
from run.module.skip import skip

class skip_Test(unittest.TestCase):

    # Public

    def test(self):
        attribute = Mock()
        self.assertEqual(skip(attribute), attribute)
        self.assertEqual(getattr(attribute, skip.attribute_name), True)
