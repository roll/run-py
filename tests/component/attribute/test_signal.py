import unittest
from run.attribute.signal import AttributeSignal

class AttributeSignalTest(unittest.TestCase):

    #Public

    def test(self):
        signal = AttributeSignal('attribute')
        self.assertEqual(signal.attribute, 'attribute') 
        