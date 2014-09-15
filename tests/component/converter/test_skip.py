import unittest
from unittest.mock import Mock
from run.converter.skip import skip


class skip_Test(unittest.TestCase):

    # Public

    def test(self):
        task = Mock()
        self.assertEqual(skip(task), task)
        self.assertEqual(getattr(task, skip.attribute_name), True)
