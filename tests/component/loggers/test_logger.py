import unittest
from importlib import import_module
component = import_module('run.loggers.logger')


@unittest.skip
class StackTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.stack = component.Stack()
        self.task1 = self.make_mock_task1_class()()
        self.task2 = self.make_mock_task2_class()()

    # Helpers

    def make_mock_task1_class(self):
        class Task1:
            # Public
            meta_module = 'module1'
            meta_name = 'task1'
            meta_qualname = '[key] module1.task1'
            def meta_format(self, attribute=None):
                return getattr(self, attribute)
        return Task1

    def make_mock_task2_class(self):
        class Task2:
            # Public
            meta_module = 'module2'
            meta_name = 'task2'
            meta_qualname = 'module2.task2'
            def meta_format(self, attribute=None):
                return getattr(self, attribute)
        return Task2

    # Tests

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
