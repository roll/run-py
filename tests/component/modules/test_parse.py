import os
import unittest
from run.modules.parse import ParseVar

class ParseVarTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.var = ParseVar(
            'test_parse.py', 'import (.*test)\n', 
            basedir=os.path.dirname(__file__),
            module=None)
    
    def test_retrieve(self):
        self.var.processors = [lambda items: items[0]]        
        self.assertEqual(self.var.retrieve(), 'unittest')
        
    def test_retrieve_exception(self):
        self.var.processors = [lambda items: 1/0]
        self.var.fallback = 'fallback'     
        self.assertEqual(self.var.retrieve(), 'fallback')        
    
    def test__search(self):
        self.assertEqual(self.var._search(), ['unittest'])
    
    def test__process(self):
        self.var.processors = [lambda x: x*2, lambda x: str(x)]
        self.assertEqual(self.var._process(2), '4')
    
    def test__fallback_exception(self):
        self.var.fallback = IndexError()
        self.assertRaises(IndexError, self.var._fallback, KeyError())
    
    def test__fallback_callable(self):
        self.var.fallback = lambda exception: 'fallback'
        self.assertEqual(self.var._fallback(KeyError()), 'fallback')
    
    def test__fallback_var(self):
        self.var.fallback = 'fallback'
        self.assertEqual(self.var._fallback(KeyError()), 'fallback')           