import unittest
from run.module.error import ModuleAttributeError

class NotFoundTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertRaises(ModuleAttributeError, self._raise)

    # Protected

    def _raise(self):
        raise ModuleAttributeError()
