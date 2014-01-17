import unittest
from unittest.mock import Mock
from run.task.method import MethodTask

class MethodTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.function = Mock(return_value='value')
        self.task = MethodTask(self.function, module='module')
        
    def test_complete(self):        
        self.assertEqual(self.task.complete(*self.args, **self.kwargs), 'value')
        self.function.assert_called_with('module', *self.args, **self.kwargs)