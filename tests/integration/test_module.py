import unittest
from io import StringIO
from unittest.mock import patch
from run.module import Module
from run.task import Task
from run.var import Var

# Tests

class ModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.stdout = self.patcher.start()
        self.addCleanup(patch.stopall)
        self.module = MockModule(meta_module=None)

    def test_list(self):
        self.module.list()
        self.assertEqual(
            self.stdout.getvalue(),
            'attribute\n'
            'class_var\n'
            'default\n'
            'info\n'
            'list\n'
            'meta\n'
            'method_task\n'
            'module\n'
            'property_var\n'
            'task\n'
            'var\n')


# Fixtures

class MockSubmodule(Module):

    # Vars

    module_var = True


class MockTask(Task):

    # Public

    def meta_invoke(self, *args, **kwargs):
        pass


class MockVar(Var):

    # Public

    def meta_invoke(self, *args, **kwargs):
        pass


class MockModule(Module):

    # Attributes

    attribute = True

    # Classes

    class class_var:
        pass

    # Meta

    meta_grayscale = True

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
