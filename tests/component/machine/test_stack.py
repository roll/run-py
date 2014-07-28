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
            meta_qualname='module1.task1')
        self.task2 = Mock(
            meta_module='module2',
            meta_name='task2',
            meta_qualname='module2.task2')

    def test_push(self):
        self.stack.push('task')
        self.assertEqual(self.stack, ['task'])

    def test_pop(self):
        self.stack.push('task')
        self.assertEqual(self.stack.pop(), 'task')
        self.assertFalse(self.stack)

    def test___repr___0_tasks(self):
        self.assertEqual(str(self.stack), '')

    def test___repr___1_tasks(self):
        self.stack.push(self.task1)
        self.assertEqual(repr(self.stack), 'module1.task1')

    def test___repr___tasks_with_same_modules(self):
        self.stack.push(self.task1)
        self.stack.push(self.task1)
        self.assertEqual(repr(self.stack),
                         'module1.task1/task1')

    def test___repr___tasks_with_different_modules(self):
        self.stack.push(self.task1)
        self.stack.push(self.task2)
        self.assertEqual(repr(self.stack),
                         'module1.task1/module2.task2')
