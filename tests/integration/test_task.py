import unittest
from io import StringIO
from unittest.mock import patch
from run.module import Module
from run.settings import settings
from run.task import task, require, trigger


# Fixtures

class MockModule(Module):

    # Tasks

    def task1(self):
        print('task1 is done')

    def task2(self):
        print('task2 is done')

    @require('task1')
    @trigger('task2')
    def task4(self):
        print('task4 is done')

    @task
    def task5(self):
        print('task5 is done')

    task5.meta_require('task1')
    task5.meta_trigger('task2')


# Cases

class DependencyTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        patch.object(settings, 'plain', True).start()
        self.stdout = patch('sys.stdout', new_callable=StringIO).start()
        self.module = MockModule(meta_build=True)

    # Tests

    def test_list(self):
        self.module.list()
        self.assertEqual(
            self.stdout.getvalue(),
            'info\n'
            'list\n'
            'meta\n'
            'task1\n'
            'task2\n'
            'task4\n'
            'task5\n')

    def test_task4(self):
        self.module.task4()
        self.assertEqual(
            self.stdout.getvalue(),
            'task1 is done\n'
            'task4 is done\n'
            'task2 is done\n')

    def test_task5(self):
        self.module.task5()
        self.assertEqual(
            self.stdout.getvalue(),
            'task1 is done\n'
            'task5 is done\n'
            'task2 is done\n')
