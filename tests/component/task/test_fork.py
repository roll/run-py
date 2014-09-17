import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.fork')


class fork_Test(unittest.TestCase):

    # Tests

    def test(self):
        args = ('arg1',)
        kwargs = {'kwarg1': 'kwarg1'}
        prototype = Mock(__meta_fork__=Mock(return_value='forked_prototype'))
        forked_prototype = component.fork(prototype, *args, **kwargs)
        self.assertEqual(forked_prototype, 'forked_prototype')
        prototype.__meta_fork__.assert_called_with(*args, **kwargs)
