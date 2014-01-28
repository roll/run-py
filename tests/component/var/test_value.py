import unittest
from run.var.value import ValueVar

class ValueVarTest(unittest.TestCase):

    #Public

    def test_invoke(self):
        var = ValueVar('value', module=None)
        self.assertEqual(var.invoke(), 'value')