========
run.task
========

Module provides task related functionality.

Public
======

Module’s public interface.

.. autoclass:: run.task.Task

Helper functions
----------------

.. autofunction:: run.task.task
.. autofunction:: run.task.module

Builtin concrete tasks:

.. autoclass:: run.task.DerivedTask
.. autoclass:: run.task.DescriptorTask
.. autoclass:: run.task.FindTask
.. autoclass:: run.task.InputTask
.. autoclass:: run.task.MethodTask
.. autoclass:: run.task.NullTask
.. autoclass:: run.task.RenderTask
.. autoclass:: run.task.SubprocessTask
.. autoclass:: run.task.ValueTask

Builtin task signals:

.. autoclass:: run.task.InitiatedTaskSignal
.. autoclass:: run.task.SuccessedTaskSignal
.. autoclass:: run.task.FailedTaskSignal