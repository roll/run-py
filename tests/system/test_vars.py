from tests.system.test_examples import ExamplesTest


class VarsTest(ExamplesTest):

    # Public

    __test__ = True

    def test_command(self):
        result = self._execute('command')
        self.assertEqual(result, 'Hello World!\nNone\n')

    def test_derived(self):
        result = self._execute('derived')
        self.assertEqual(result, 'Hello World!\nNone\n')

    def test_descriptor(self):
        result = self._execute('descriptor')
        self.assertEqual(result, 'True\n')

    def test_find(self):
        result = self._execute('find')
        self.assertEqual(result, 'find\n')

    def test_function(self):
        result = self._execute('function')
        self.assertRegex(result, '.*examples/path\n')

    def test_list(self):
        result = self._execute('list')
        self.assertEqual(
            result,
            'command\n'
            'command_task\n'
            'derived\n'
            'descriptor\n'
            'find\n'
            'function\n'
            'info\n'
            'list\n'
            'meta\n')

    # Protected

    @property
    def _file(self):
        return 'vars.py'
