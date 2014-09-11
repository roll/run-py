from tests.system.test_examples import ExamplesTest


class TasksTest(ExamplesTest):

    # Public

    __test__ = True

    def test_default(self):
        result = self._execute()
        self.assertEqual(
            result,
            'derived\n'
            'descriptor\n'
            'find\n'
            'function\n'
            'info\n'
            'list\n'
            'meta\n'
            'null\n'
            'subprocess\n')

    def test_derived(self):
        result = self._execute('derived')
        self.assertEqual(result, 'Hello World!\n')

    def test_descriptor(self):
        result = self._execute('descriptor')
        self.assertEqual(result, 'True\n')

    def test_find(self):
        result = self._execute('find')
        self.assertEqual(result, 'find\n')

    def test_function(self):
        result = self._execute('function path')
        self.assertRegex(result, '.*examples/path\n')

    def test_info(self):
        result = self._execute('info list')
        self.assertRegex(result, 'list.*')

    def test_list(self):
        result = self._execute('list')
        self.assertEqual(len(result.splitlines()), 9)

    def test_meta(self):
        result = self._execute('meta list')
        self.assertRegex(result, ".*'type': 'FunctionTask'}\n")

    def test_null(self):
        result = self._execute('null')
        self.assertEqual(result, 'Hello World!\n')

    def test_subprocess(self):
        result = self._execute('subprocess')
        self.assertEqual(result, 'Hello World!\n')

    # Protected

    @property
    def _file(self):
        return 'tasks.py'
