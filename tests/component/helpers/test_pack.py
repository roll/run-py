import unittest
from importlib import import_module
component = import_module('run.helpers.pack')


class pack_Test(unittest.TestCase):

    # Tests

    def test(self):
        self.assertEqual(component.pack(1, a='a'), "(1, a='a')")
