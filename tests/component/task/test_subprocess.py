import unittest
from unittest.mock import Mock, patch
from run.task.subprocess import SubprocessTask

class SubprocessTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.task = SubprocessTask(meta_module=None)
        self.process = Mock(wait=Mock(return_value=0))
        self.Popen = Mock(return_value=self.process)
        patch('subprocess.Popen', self.Popen).start()
        self.addCleanup(patch.stopall)
        
    def test___call__(self):
        self.task('command')
        self.Popen.assert_called_with('command', shell=True)
        
    def test___call___with_prefix_and_separator(self):
        self.task('command', prefix='prefix', separator='_')
        self.Popen.assert_called_with('prefix_command', shell=True)
        
    def test___call___when_returncode_is_not_zero(self):
        self.process.wait.return_value = 1
        self.assertRaises(RuntimeError, self.task)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)