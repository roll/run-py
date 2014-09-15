import unittest
from run.converter.result import Result


class ResultTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(Result, object))