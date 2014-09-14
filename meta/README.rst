{% extends "packgram/README.rst" %}

{% block badges %}
{{ super() }}

Example
-------

The real simple example introduces some functionality. 

- create runfile.py in current working directory:

  .. code-block:: python

    from run import Module, DialogVar, require, trigger
    
    class Module(Module):
        
        #Tasks
        
        def ready(self):
            print('We are ready to say', self.greeting, 'to person.')
        
        @require('ready')
        @trigger('done')
        def greet(self, person, times=3):
            """Greet the given person."""
            print(self.greeting, person, str(times), 'times!')
            
        def done(self):
            print('We are done.')
            
        #Vars
        
        greeting = DialogVar(
            question='Type your greeting: ',
            default='Hello',
        )
	    
- get run attributes list from command line:

  .. code-block:: bash

    $ run
    default
    done
    greet
    greeting
    info
    list
    meta
    ready

- autocomplete attribute from command line:

  .. code-block:: bash

    $ run g<TAB>
    $ run greet
    
- get attribute infomation from command line:

  .. code-block:: bash

    $ run greet -i
    greet(person='World', times=3)
    ---
    Type: MethodTask
    Dependencies: [trigger <MethodTask "done">, require <MethodTask "ready">]
    Default arguments: ()
    Default keyword arguments: {}
    ---
    Greet the given person.

- run task from command line:

  .. code-block:: bash

    $ run greet Rachel, times=5
    Type your greeting ([Hello]/*): <Hi>
    We are ready to say Hi to person.
    Hi Rachel 5 times!
    We are done.
	
More usefull example you can find here:

- `Base module <https://github.com/respect31/packgram/blob/master/packgram/manage.py>`_
- `Base templates <https://github.com/respect31/packgram/blob/master/packgram/_sources>`_
- `Run's module <https://github.com/respect31/run/blob/master/runfile.py>`_
- `Run's templates <https://github.com/respect31/run/tree/master/_sources>`_

That's how run builds himself using module inheritance.
{% endblock %}