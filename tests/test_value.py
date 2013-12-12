import os
import unittest
from sub import ParsedValue

class FetchTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.value = ParsedValue('test_value.py', 'import (.*test)\n', 
                                 base_dir=os.path.dirname(__file__))
    
    def test_get(self):
        self.value.processors = [lambda items: items[0]]        
        self.assertEqual(self.value.get(), 'unittest')
        
    def test_fetch_exception(self):
        self.value.processors = [lambda items: 1/0]
        self.value.fallback = 'fallback'     
        self.assertEqual(self.value.get(), 'fallback')        
    
    def test__search(self):
        self.assertEqual(self.value._search(), ['unittest'])
    
    def test__process(self):
        self.value.processors = [lambda x: x*2, lambda x: str(x)]
        self.assertEqual(self.value._process(2), '4')
    
    def test__fallback_exception(self):
        self.value.fallback = IndexError()
        self.assertRaises(IndexError, self.value._fallback, KeyError())
    
    def test__fallback_callable(self):
        self.value.fallback = lambda exception: 'fallback'
        self.assertEqual(self.value._fallback(KeyError()), 'fallback')
    
    def test__fallback_value(self):
        self.value.fallback = 'fallback'
        self.assertEqual(self.value._fallback(KeyError()), 'fallback')           