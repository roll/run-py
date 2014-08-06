import unittest
from unittest.mock import Mock
from run.dependency.depend import depend


class depend_Test(unittest.TestCase):

    # Public

    def test(self):
        dependency = Mock()
        method = Mock()
        result = depend(dependency)(method)
        self.assertEqual(result, dependency.return_value)
        # Check dependency call
        dependency.assert_called_with(method)
