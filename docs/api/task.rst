========
run.task
========

Module provides task related functionality.

Public
======

Module’s public interface.

Base class
----------

.. autoclass:: run.task.Task

Concrete tasks
--------------

.. autoclass:: run.task.DerivedTask
.. autoclass:: run.task.DescriptorTask
.. autoclass:: run.task.FindTask
.. autoclass:: run.task.FunctionTask
.. autoclass:: run.task.InputTask
.. autoclass:: run.task.MethodTask
.. autoclass:: run.task.NullTask
.. autoclass:: run.task.RenderTask
.. autoclass:: run.task.SubprocessTask

Signal classes
--------------

.. autoclass:: run.task.InitiatedTaskSignal
.. autoclass:: run.task.SuccessedTaskSignal
.. autoclass:: run.task.FailedTaskSignal

Helper functions
----------------

.. autofunction:: run.task.task