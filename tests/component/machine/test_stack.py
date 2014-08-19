import unittest
from unittest.mock import Mock
from run.machine.stack import Stack


class StackTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.stack = Stack()
        self.task1 = Mock(
            meta_module='module1',
            meta_name='task1',
            meta_fullname='[key] module1.task1',
            meta_format=lambda string: string)
        self.task2 = Mock(
            meta_module='module2',
            meta_name='task2',
            meta_qualname='module2.task2',
            meta_format=lambda string: string)

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
