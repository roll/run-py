import unittest
from functools import partial
from unittest.mock import Mock
from run.modules.input import InputVar

class InputVarTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.var_draft = partial(InputVar, 'prompt', module=None)
    
    def test_retireve(self):
        input_operator = Mock(return_value='input')
        var = self.var_draft(input_operator=input_operator)
        self.assertEqual(var.retrieve(), 'input')
        input_operator.assert_called_with('prompt')
        
    def test_retireve_with_default(self):
        input_operator = Mock(return_value='')
        var = self.var_draft(default='default', input_operator=input_operator)
        self.assertEqual(var.retrieve(), 'default')
    
    def test_retireve_with_options(self):
        input_operator = Mock(return_value='')
        print_operator = Mock()
        var = self.var_draft(options=['option'], 
            input_operator=input_operator,
            print_operator=print_operator)
        self.assertRaises(ValueError, var.retrieve)
        print_operator.assert_called_with('Try again..')