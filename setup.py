#DO NOT CHANGE THIS FILE. SOURCE IS IN "_sources" DIRECTORY.

import os
from setuptools import find_packages, setup

package = {

	#Main

    'name': 'runpack',
	'version':'0.13.1',
	'packages': find_packages(
        os.path.dirname(__file__) or '.', 
        exclude=['tests*']
    ),
	'include_package_data': True,
    'install_requires': ['box>=0.17', 'jinja2'],  
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': 'roll',
    'author_email': 'roll@respect31.com',
    'classifiers': ['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: System :: Systems Administration'],       
    'description': 'Run is a program to run tasks from files.',
    'download_url':'https://github.com/respect31/run/tarball/0.13.1',
    'license': 'MIT License',
    'maintainer': 'roll',
    'maintainer_email': 'roll@respect31.com',
    'platforms': ['Unix'],
    'url': 'https://github.com/respect31/run',
    'long_description': '''.. DO NOT CHANGE THIS FILE. SOURCE IS IN "_sources" DIRECTORY.

Run
=====================
Run is a program to run tasks from files.

.. image:: https://secure.travis-ci.org/respect31/run.png?branch=master 
     :target: https://travis-ci.org/respect31/run 
     :alt: build
.. image:: https://coveralls.io/repos/respect31/run/badge.png?branch=master 
     :target: https://coveralls.io/r/respect31/run  
     :alt: coverage
.. image:: http://b.repl.ca/v1/docs-uploaded-brightgreen.png
     :target: http://run.readthedocs.org
     :alt: documentation
     
Quick Links
-----------
- `Source code (GitHub) <https://github.com/respect31/run>`_
- `Package index (PyPi) <https://pypi.python.org/pypi?:action=display&name=runpack>`_

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install runpack

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

- `Base module <https://github.com/respect31/packgram/blob/master/packgram/manage/python.py>`_
- `Run's module <https://github.com/respect31/run/blob/master/runfile.py>`_
- `Run's templates <https://github.com/respect31/run/tree/master/_sources>`_

That's how run builds himself using module inheritance.
        
Authors
-------
- roll <roll@respect31.com>

Maintainers
-----------
- roll <roll@respect31.com>

License
-------
MIT License
`````````````
Copyright (c) 2014 Respect31 <post@respect31.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.''',  
    
}

if (not os.environ.get('TRAVIS', None) and  
	not	os.environ.get('READTHEDOCS', None)):
	package['entry_points'] = {'console_scripts': ['run = run:program']}
	package['data_files'] = [('/etc/bash_completion.d', ['data/run.sh'])]	

if __name__ == '__main__':
	setup(**package)