import unittest
from unittest.mock import Mock
from run.dependency.resolver import CommonResolver

class CommonResolverTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.attribute = Mock()
        self.Resolver = self._make_mock_resolver()
        self.resolver = self.Resolver('task', *self.args, **self.kwargs)
        self.resolver.bind(self.attribute)

    def test___repr__(self):
        self.assertEqual(repr(self.resolver), "task('arg1', kwarg1='kwarg1')")

    def test___repr__not_bound(self):
        self.resolver.bind(None)
        self.assertRaises(RuntimeError, repr, self.resolver)

    # Protected

    def _make_mock_resolver(self):
        class MockResolver(CommonResolver):
            # Protected
            _getattribute = Mock(return_value='task')
            _task_class = Mock()
        return MockResolver

