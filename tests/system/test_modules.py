from tests.system.test_demo import DemoTest


class ModulesTest(DemoTest):

    # Actions

    __test__ = True

    # Helpers

    # override
    @property
    def filename(self):
        return 'modules.py'

    # Tests

    def test_command_list(self):
        result = self.execute('command.list')
        self.assertEqual(
            result,
            'command.goodbye\n'
            'command.hello\n'
            'command.info\n'
            'command.list\n'
            'command.meta\n')

    def test_command_hello(self):
        result = self.execute('command.hello')
        self.assertEqual(result, 'Hello World!\n')

    def test_find_list(self):
        result = self.execute('find.list')
        self.assertEqual(
            result,
            'find.command\n'
            'find.descriptor\n'
            'find.find\n'
            'find.function\n'
            'find.info\n'
            'find.list\n'
            'find.meta\n'
            'find.null\n'
            'find.proxy\n')

    def test_function_list(self):
        result = self.execute('function.list')
        self.assertEqual(
            result,
            'function.gcd\n'
            'function.info\n'
            'function.list\n'
            'function.meta\n')

    def test_function_gcd(self):
        result = self.execute('function.gcd 10,15')
        self.assertEqual(result, '5\n')