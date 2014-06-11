=======
run.var
=======

Module provides var related functionality.

Public
======

Module’s public interface.

Base class
----------

.. autoclass:: run.var.Var

Helper functions
----------------

.. autofunction:: run.var.var

Concrete vars
-------------

.. autoclass:: run.var.DerivedVar
.. autoclass:: run.var.DescriptorVar
.. autoclass:: run.var.FindVar
.. autoclass:: run.var.FunctionVar
.. autoclass:: run.var.InputVar
.. autoclass:: run.var.MethodVar
.. autoclass:: run.var.NullVar
.. autoclass:: run.var.RenderVar
.. autoclass:: run.var.SubprocessVar
.. autoclass:: run.var.ValueVar

Var signals
-----------

.. autoclass:: run.var.InitiatedVarSignal
.. autoclass:: run.var.SuccessedVarSignal
.. autoclass:: run.var.FailedVarSignal