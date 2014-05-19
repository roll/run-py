{% extends "packgram/README.rst" %}

{% block installation %}
{{ super() }}
Example
-------

The real simple example introduces some functionality. 

- create runfile.py in current working directory:

  .. code-block:: python

    from run import Module, InputVar, require, trigger
    
    class MainModule(Module):
        
        #Tasks
        
        def ready(self):
            print('Your choice is "{greeting}".\n'
                  'We\'re ready.'.format(
                greeting=self.greeting,))    
        
        @require('ready')
        @trigger('done')
        def greet(self, person='World', times=1):
            """Greet the given person."""
            for _ in range(times):
                print('{greeting} {person}!'.format(
                    greeting=self.greeting, 
                    person=person))
            
        def done(self):
            print('OK. We\'re done.')
            
        #Vars
        
        greeting = InputVar(
            prompt='Type your greeting',
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

    $ run li<TAB>
    $ run list
    
- get attribute infomation from command line:

  .. code-block:: bash

    $ run greet -i
    greet(person='World', times=1)
    ---
    Type: MethodTask
    Dependencies: [trigger <MethodTask "done">, require <MethodTask "ready">]
    Default arguments: ()
    Default keyword arguments: {}
    ---
    Greet the given person


- run task from command line:

  .. code-block:: bash

    $ run greet Rachel, times=3
    Type your greeting [Hello]: <Hi>
    Your choice is "Hi".
    We're ready.
    Hi Rachel!
    Hi Rachel!
    Hi Rachel!
    OK. We're done.
	
More usefull example you can find here:

- `Base module <https://github.com/respect31/packgram/blob/master/packgram/manage.py>`_
- `Base templates <https://github.com/respect31/packgram/blob/master/packgram/_sources>`_
- `Run's module <https://github.com/respect31/run/blob/master/runfile.py>`_
- `Run's templates <https://github.com/respect31/run/tree/master/_sources>`_

That's how run builds himself using module inheritance.
{% endblock %}