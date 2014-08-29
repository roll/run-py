#TO MAKE CHANGES USE "_sources" DIRECTORY (see packgram docs).

import os
from setuptools import find_packages

package = {

    #Main

    'name': 'runpack',
    'version':'0.26.0',
    'packages': find_packages(
        os.path.dirname(__file__) or '.', 
        exclude=['tests*']
    ),
    'include_package_data': True,
    'install_requires': ['box>=0.36'],  
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': 'roll',
    'author_email': 'roll@respect31.com',
    'classifiers': ['Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: System :: Systems Administration'],       
    'description': 'Run is a program to run tasks from files.',
    'download_url':'https://github.com/respect31/run/tarball/0.26.0',
    'license': 'MIT License',
    'maintainer': 'roll',
    'maintainer_email': 'roll@respect31.com',
    'platforms': ['Unix'],
    'url': 'https://github.com/respect31/run',
    'long_description': '''.. TO MAKE CHANGES USE "_sources" DIRECTORY (see packgram docs).

Run
=====================
Run is a program to run tasks from files.

.. image:: http://img.shields.io/badge/code-GitHub-brightgreen.svg
     :target: https://github.com/respect31/run
     :alt: code
.. image:: http://img.shields.io/travis/respect31/run/master.svg
     :target: https://travis-ci.org/respect31/run 
     :alt: build
.. image:: http://img.shields.io/coveralls/respect31/run/master.svg 
     :target: https://coveralls.io/r/respect31/run  
     :alt: coverage
.. image:: http://img.shields.io/badge/docs-RTD-brightgreen.svg
     :target: http://run.readthedocs.org
     :alt: docs     
.. image:: http://img.shields.io/pypi/v/runpack.svg
     :target: https://pypi.python.org/pypi?:action=display&name=runpack
     :alt: pypi


Example
-------

The real simple example introduces some functionality. 

- create runfile.py in current working directory:

  .. code-block:: python

    from run import Module, InputVar, require, trigger
    
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
    Type your greeting (Hello): <Hi>
    We are ready to say Hi to person.
    Hi Rachel 5 times!
    We are done.
	
More usefull example you can find here:

- `Base module <https://github.com/respect31/packgram/blob/master/packgram/manage.py>`_
- `Base templates <https://github.com/respect31/packgram/blob/master/packgram/_sources>`_
- `Run's module <https://github.com/respect31/run/blob/master/runfile.py>`_
- `Run's templates <https://github.com/respect31/run/tree/master/_sources>`_

That's how run builds himself using module inheritance.

Application
-----------
Package is under active development and is not ready for production use.
Backward-compatibility between minor releases (0.x.0), documentation and 
changelog are not guaranteed to be present before stable versions (>=1.0.0).

Requirements
------------
- Platforms

  - Unix
- Interpreters

  - Python 3.3
  - Python 3.4

Installation
------------
- pip install runpack

Contribution
------------
- Authors

  - roll <roll@respect31.com>
- Maintainers

  - roll <roll@respect31.com>

Changelog
---------
- no entries yet

License
-------
**MIT License**

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
THE SOFTWARE.
''',  
}

if (not os.environ.get('TRAVIS', None) and  
    not os.environ.get('READTHEDOCS', None)):
    package['entry_points'] = {'console_scripts': ['run = run.program:program']}
    package['data_files'] = [('/etc/bash_completion.d', ['data/run.sh'])]

if __name__ == '__main__':
    from setuptools import setup
    setup(**package)
