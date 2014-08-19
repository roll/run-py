import unittest
from run.machine.stack import Stack


class StackTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.stack = Stack()
        self.task1 = self._make_mock_task1_class()()
        self.task2 = self._make_mock_task2_class()()

    def test_push(self):
        self.stack.push('task')
        self.assertEqual(self.stack, ['task'])

    def test_pop(self):
        self.stack.push('task')
        self.assertEqual(self.stack.pop(), 'task')
        self.assertFalse(self.stack)

    def test_format_0_tasks(self):
        self.assertEqual(self.stack.format(), '')

    def test_format_1_tasks(self):
        self.stack.push(self.task1)
        self.assertEqual(self.stack.format(),
                         '[key] module1.task1')

    def test_format_tasks_with_same_modules(self):
        self.stack.push(self.task1)
        self.stack.push(self.task1)
        self.assertEqual(self.stack.format(),
                         '[key] module1.task1/task1')

    def test_format_tasks_with_different_modules(self):
        self.stack.push(self.task1)
        self.stack.push(self.task2)
        self.assertEqual(self.stack.format(),
                         '[key] module1.task1/module2.task2')

    # Protected

    def _make_mock_task1_class(self):
        class Task1:
            # Public
            meta_module = 'module1'
            meta_name = 'task1'
            meta_fullname = '[key] module1.task1'
            def meta_format(self, mode='name'):
                return getattr(self, 'meta_' + mode)
        return Task1

    def _make_mock_task2_class(self):
        class Task2:
            # Public
            meta_module = 'module2'
            meta_name = 'task2'
            meta_qualname = 'module2.task2'
            def meta_format(self, mode='name'):
                return getattr(self, 'meta_' + mode)
        return Task2
