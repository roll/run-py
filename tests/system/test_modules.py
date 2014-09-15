from tests.system.test_examples import ExamplesTest


class ModulesTest(ExamplesTest):

    # Public

    __test__ = True

    def test_auto_list(self):
        result = self._execute('auto.list')
        self.assertEqual(
            result,
            'auto.gcd\n'
            'auto.info\n'
            'auto.list\n'
            'auto.meta\n')

    def test_auto_gcd(self):
        result = self._execute('auto.gcd 10,15')
        self.assertEqual(result, '5\n')

    def test_command_list(self):
        result = self._execute('command.list')
        self.assertEqual(
            result,
            'command.goodbye\n'
            'command.hello\n'
            'command.info\n'
            'command.list\n'
            'command.meta\n')

    def test_command_hello(self):
        result = self._execute('command.hello')
        self.assertEqual(result, 'Hello World!\n')

    def test_find_list(self):
        result = self._execute('find.list')
        self.assertEqual(
            result,
            'find.command\n'
            'find.derived\n'
            'find.descriptor\n'
            'find.find\n'
            'find.function\n'
            'find.info\n'
            'find.list\n'
            'find.meta\n'
            'find.null\n')

    # Protected

    @property
    def _file(self):
        return 'modules.py'
