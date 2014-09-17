import unittest
from unittest.mock import Mock
from run.task.update import Update


class UpdateTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.update = Update('method', 'value')

    def test_apply(self):
        task = Mock()
        self.update.apply(task)
        task.method.assert_called_with('value')
