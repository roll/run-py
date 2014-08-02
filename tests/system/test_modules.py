from tests.system.test_examples import ExamplesTest

class ModulesTest(ExamplesTest):

    # Public

    __test__ = True

    def test_auto_list(self):
        result = self._execute('auto.list')
        self.assertEqual(
            result,
            'default\n'
            'gcd\n'
            'info\n'
            'list\n'
            'meta\n')

    def test_auto_gcd(self):
        result = self._execute('auto.gcd 10,15')
        self.assertEqual(result, '5\n')

    def test_find_list(self):
        result = self._execute('find.list')
        self.assertEqual(
            result,
            'default\n'
            'derived\n'
            'descriptor\n'
            'find\n'
            'function\n'
            'info\n'
            'input\n'
            'list\n'
            'meta\n'
            'method\n'
            'null\n'
            'render\n'
            'subprocess\n')

    def test_subprocess_list(self):
        result = self._execute('subprocess.list')
        self.assertEqual(
            result,
            'default\n'
            'goodbye\n'
            'hello\n'
            'info\n'
            'list\n'
            'meta\n')

    def test_subprocess_hello(self):
        result = self._execute('subprocess.hello')
        self.assertEqual(result, 'Hello World!\n')

    # Protected

    @property
    def _file(self):
        return 'modules.py'
