import unittest
from run.attribute.signal import AttributeSignal

class AttributeSignalTest(unittest.TestCase):

    #Public

    def test_attribute(self):
        signal = AttributeSignal('attribute')
        self.assertEqual(signal.attribute, 'attribute') 
        