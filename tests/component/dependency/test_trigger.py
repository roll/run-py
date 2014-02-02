from run.dependency.trigger import trigger

class trigger_Test(TaskConstraintTest):

    #Public

    def test__apply_dependency(self):
        tasks = ['task1', 'task2']
        builder = self.constraint._attribute_class()
        constraint = trigger(tasks)
        constraint._apply_dependency(builder)
        builder.trigger.assert_called_with(tasks)  