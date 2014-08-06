import unittest
from unittest.mock import Mock
from run.task.fork import fork


class fork_Test(unittest.TestCase):

    # Public

    def test(self):
        args = ('arg1',)
        kwargs = {'kwarg1': 'kwarg1'}
        prototype = Mock(__fork__=Mock(return_value='forked_prototype'))
        forked_prototype = fork(prototype, *args, **kwargs)
        self.assertEqual(forked_prototype, 'forked_prototype')
        prototype.__fork__.assert_called_with(*args, **kwargs)
