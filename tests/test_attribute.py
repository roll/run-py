import unittest
from run import AttributeMetadata, Task
        
class AttributeMetadataHelp(unittest.TestCase):

    #Public

    def test(self):
        builder = Task()
        attribute = builder()
        metadata = AttributeMetadata(
            attribute, signature='signature', docstring='docstring')
        self.assertEqual(metadata.name, '')
        self.assertEqual(metadata.module_name, '')
        self.assertEqual(metadata.attribute_name, '')
        self.assertEqual(metadata.help, 'signature\ndocstring')
        self.assertEqual(metadata.signature, 'signature')
        self.assertEqual(metadata.docstring, 'docstring')