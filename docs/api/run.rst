===
run
===

Module provides program's end-user functionality.

------
Public
------

Module’s public interface.

Module class
============

- :class:`run.Module <run.module.Module>`

Helper functions
================

- :func:`run.fork <run.attribute.fork>`
- :class:`run.depend <run.dependency.depend>`
- :class:`run.require <run.dependency.require>`
- :class:`run.trigger <run.dependency.trigger>`
- :func:`run.skip <run.module.skip>`
- :func:`run.task <run.task.task>`
- :func:`run.module <run.task.module>`
- :func:`run.var <run.var.var>`
     
Builtin attributes
==================

Modules
-------

- :class:`run.AutoModule <run.module.AutoModule>`
- :class:`run.FindModule <run.module.FindModule>`
- :class:`run.NullModule <run.module.NullModule>`
- :class:`run.SubprocessModule <run.module.SubprocessModule>`

Tasks
-----

- :class:`run.DerivedTask <run.task.DerivedTask>`
- :class:`run.DescriptorTask <run.task.DescriptorTask>`
- :class:`run.FindTask <run.task.FindTask>`
- :class:`run.FunctionTask <run.task.FunctionTask>`
- :class:`run.InputTask <run.task.InputTask>`
- :class:`run.MethodTask <run.task.MethodTask>`
- :class:`run.NullTask <run.task.NullTask>`
- :class:`run.RenderTask <run.task.RenderTask>`
- :class:`run.SubprocessTask <run.task.SubprocessTask>`
- :class:`run.ValueTask <run.task.ValueTask>`

Vars
----

- :class:`run.DerivedVar <run.var.DerivedVar>`
- :class:`run.DescriptorVar <run.var.DescriptorVar>`
- :class:`run.FindVar <run.var.FindVar>`
- :class:`run.FunctionVar <run.var.FunctionVar>`
- :class:`run.InputVar <run.var.InputVar>`
- :class:`run.MethodVar <run.var.MethodVar>`
- :class:`run.NullVar <run.var.NullVar>`
- :class:`run.RenderVar <run.var.RenderVar>`
- :class:`run.SubprocessVar <run.var.SubprocessVar>`
- :class:`run.ValueVar <run.var.ValueVar>`

Settings
========

- :data:`run.settings <run.settings.settings>`

Version
=======

.. autodata:: run.version

--------
Internal
--------

Module’s internal implementation.

.. autoclass:: run.version.Version