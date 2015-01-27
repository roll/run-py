import unittest
from io import StringIO
from unittest.mock import patch
from run.module import Module
from run.settings import settings
from run.task import Task
from run.var import Var


# Fixtures

class MockSubmodule(Module):

    # Vars

    module_var = True


class MockTask(Task):

    # Public

    def Invoke(self, *args, **kwargs):
        pass


class MockVar(Var):

    # Public

    def Invoke(self, *args, **kwargs):
        pass


class MockModule(Module):

    # Data

    attribute = True

    # Classes

    class class_var:
        pass

    # Modules

    module = MockSubmodule()

    # Tasks

    task = MockTask()

    def method_task(self):
        pass

    # Vars

    var = MockVar()

    @property
    def property_var(self):
        pass


# Cases

class ModuleTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        patch.object(settings, 'plain', True).start()
        self.stdout = patch('sys.stdout', new_callable=StringIO).start()
        self.module = MockModule(Build=True)

    # Tests

    def test_list(self):
        self.module.list()
        self.assertEqual(
            self.stdout.getvalue(),
            'attribute\n'
            'class_var\n'
            'info\n'
            'list\n'
            'meta\n'
            'method_task\n'
            'module\n'
            'property_var\n'
            'task\n'
            'var\n')
