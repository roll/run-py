from tests.system.test_demo import DemoTest


class VarsTest(DemoTest):

    # Actions

    __test__ = True

    # Helpers

    # override
    @property
    def filename(self):
        return 'vars.py'

    # Tests

    def test_command(self):
        result = self.execute('command')
        self.assertEqual(result, 'Hello World!\nNone\n')

    def test_descriptor(self):
        result = self.execute('descriptor')
        self.assertEqual(result, 'True\n')

    def test_find(self):
        result = self.execute('find')
        self.assertEqual(result, 'find\n')

    def test_list(self):
        result = self.execute('list')
        self.assertEqual(
            result,
            'command\n'
            'command_task\n'
            'descriptor\n'
            'find\n'
            'info\n'
            'list\n'
            'meta\n')
