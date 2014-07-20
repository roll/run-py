import unittest
from run.dependency.dependency import Dependency

class DependencyTest(unittest.TestCase):

    # Public

    def setUp(self):
        pass

    def test(self):
        pass

#     # Public
#
#     def setUp(self):
#         self.args = ('arg1',)
#         self.kwargs = {'kwarg1': 'kwarg1'}
#         self.attribute = Mock()
#         self.Resolver = self._make_mock_resolver()
#         self.resolver = self.Resolver('task', *self.args, **self.kwargs)
#         self.resolver.bind(self.attribute)
#
#     def test___repr__(self):
#         self.assertEqual(repr(self.resolver), "task('arg1', kwarg1='kwarg1')")
#
#     def test___repr__not_bound(self):
#         self.resolver.bind(None)
#         self.assertRaises(RuntimeError, repr, self.resolver)
#
#     def test_enable(self):
#         self.Resolver._task = Mock()
#         self.resolver.disable('task')
#         self.resolver.enable('task')
#         self.resolver.resolve()
#         # Check task call
#         self.assertTrue(self.Resolver._task.called)
#
#     def test_disable(self):
#         self.Resolver._task = Mock()
#         self.resolver.enable('task')
#         self.resolver.disable('task')
#         self.resolver.resolve()
#         # Check task call
#         self.assertFalse(self.Resolver._task.called)
#
#     def test_resolve(self):
#         self.resolver.resolve()
#         # Check getattribute call
#         self.resolver._getattribute.assert_called_with(
#             self.attribute.meta_module, 'task',
#             category=self.resolver._task_class, getvalue=True)
#         # Check getattribute return value (task) call
#         self.resolver._getattribute.return_value.assert_called_with(
#             *self.args, **self.kwargs)
#
#     # Protected
#
#     def _make_mock_resolver(self):
#         class MockResolver(CommonResolver):
#             # Protected
#             _getattribute = Mock(return_value=
#                 Mock(__repr__=lambda self: 'task'))
#             _task_class = Mock()
#         return MockResolver
