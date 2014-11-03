from tests.system.test_demo import DemoTest


class TasksTest(DemoTest):

    # Actions

    __test__ = True

    # Helpers

    # override
    @property
    def filename(self):
        return 'tasks.py'

    # Tests

    def test_command(self):
        result = self.execute('command')
        self.assertEqual(result, 'Hello World!\n')

    def test_find(self):
        result = self.execute('find')
        self.assertEqual(result, 'find\n')

    def test_function(self):
        result = self.execute('function path')
        self.assertRegex(result, '.*demo/path\n')

    def test_info(self):
        result = self.execute('info list')
        self.assertRegex(result, 'list.*')

    def test_list(self):
        result = self.execute('list')
        self.assertEqual(
            result,
            'command\n'
            'find\n'
            'function\n'
            'info\n'
            'list\n'
            'meta\n'
            'task\n')

    def test_meta(self):
        result = self.execute('meta list')
        self.assertRegex(result, "^{'args'.*")

    def test_task(self):
        result = self.execute('task')
        self.assertEqual(result, 'Hello World!\n')
