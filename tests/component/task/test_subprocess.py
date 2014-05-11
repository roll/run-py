import unittest
from run.task.subprocess import SubprocessTask

class SubprocessTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.task = SubprocessTask(meta_module=None)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)