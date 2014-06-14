===
run
===

Module provides program's end-user functionality.

------
Public
------

Module’s public interface.

Hierarhy of attributes
======================

.. autoclass:: run.Attribute
.. autoclass:: run.Module
.. autoclass:: run.Task
.. autoclass:: run.Var

Helper functions
================

.. autofunction:: run.fork
.. autoclass:: run.depend
.. autoclass:: run.require
.. autoclass:: run.trigger
.. autofunction:: run.skip
.. autofunction:: run.task
.. autofunction:: run.module
.. autofunction:: run.var
     
Builtin attributes
==================

Modules
-------

.. autoclass:: run.AutoModule
.. autoclass:: run.FindModule
.. autoclass:: run.NullModule
.. autoclass:: run.SubprocessModule

Tasks
-----

.. autoclass:: run.DerivedTask
.. autoclass:: run.DescriptorTask
.. autoclass:: run.FindTask
.. autoclass:: run.FunctionTask
.. autoclass:: run.InputTask
.. autoclass:: run.MethodTask
.. autoclass:: run.NullTask
.. autoclass:: run.RenderTask
.. autoclass:: run.SubprocessTask
.. autoclass:: run.ValueTask

Vars
----

.. autoclass:: run.DerivedVar
.. autoclass:: run.DescriptorVar
.. autoclass:: run.FindVar
.. autoclass:: run.FunctionVar
.. autoclass:: run.InputVar
.. autoclass:: run.MethodVar
.. autoclass:: run.NullVar
.. autoclass:: run.RenderVar
.. autoclass:: run.SubprocessVar
.. autoclass:: run.ValueVar

Settings
========

.. autodata:: run.settings

Version
=======

.. autodata:: run.version 

--------
Internal
--------

Module’s internal implementation.

.. autoclass:: run.settings.Settings
.. autoclass:: run.version.Version