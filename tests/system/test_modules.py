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

    def test_find_list(self):
        result = self._execute('find.list')
        self.assertEqual(
            result,
            'find.derived\n'
            'find.descriptor\n'
            'find.find\n'
            'find.function\n'
            'find.info\n'
            'find.input\n'
            'find.list\n'
            'find.meta\n'
            'find.null\n'
            'find.subprocess\n')

    def test_subprocess_list(self):
        result = self._execute('subprocess.list')
        self.assertEqual(
            result,
            'subprocess.goodbye\n'
            'subprocess.hello\n'
            'subprocess.info\n'
            'subprocess.list\n'
            'subprocess.meta\n')

    def test_subprocess_hello(self):
        result = self._execute('subprocess.hello')
        self.assertEqual(result, 'Hello World!\n')

    # Protected

    @property
    def _file(self):
        return 'modules.py'
