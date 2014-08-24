from tests.system.test_examples import ExamplesTest


class VarsTest(ExamplesTest):

    # Public

    __test__ = True

    def test_default(self):
        result = self._execute()
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
            'subprocess\n'
            'subprocess_task\n')

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

    def test_input(self):
        # TODO: implement
        pass

    def test_method(self):
        result = self._execute('method')
        self.assertEqual(result, 'Hello World!\n')

    def test_null(self):
        result = self._execute('method')
        self.assertEqual(result, 'Hello World!\n')

    def test_subprocess(self):
        result = self._execute('subprocess')
        self.assertEqual(result, 'Hello World!\nNone\n')

    # Protected

    @property
    def _file(self):
        return 'vars.py'
