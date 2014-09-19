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

    def test_function(self):
        result = self.execute('function')
        self.assertRegex(result, '.*demo/path\n')

    def test_list(self):
        result = self.execute('list')
        self.assertEqual(
            result,
            'command\n'
            'command_task\n'
            'descriptor\n'
            'find\n'
            'function\n'
            'info\n'
            'list\n'
            'meta\n'
            'proxy\n')

    def test_proxy(self):
        result = self.execute('proxy')
        self.assertEqual(result, 'Hello World!\nNone\n')