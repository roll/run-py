from run.dependency.require import require

class require_Test(TaskConstraintTest):

    #Public

    def test__apply_dependency(self):
        tasks = ['task1', 'task2']
        builder = self.constraint._attribute_class()
        constraint = require(tasks)
        constraint._apply_dependency(builder)
        builder.require.assert_called_with(tasks)