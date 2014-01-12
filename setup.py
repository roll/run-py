#Builded for run 0.8.1 from _templates/setup.tpl

import os
from setuptools import find_packages, setup

package = {

	#Main

    'name': 'runpack',
	'version':'0.8.1',
	'packages': find_packages(
        os.path.dirname(__file__) or '.', 
        exclude=['tests*']
    ),
	'include_package_data': True,
	'data_files': [('/etc/bash_completion.d', ['data/run.sh'])],
    'entry_points': {'console_scripts': ['run = run:program']},
    'install_requires': ['box>=0.8', 'jinja2>=2.7'],  
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': 'roll',
    'author_email': 'roll@respect31.com',
    'classifiers': ['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: System :: Systems Administration'],       
    'description': 'Run is program to run tasks from files.',
    'download_url':'https://github.com/respect31/run/tarball/0.8.1',
    'license': 'MIT License',
    'maintainer': 'roll',
    'maintainer_email': 'roll@respect31.com',
    'platforms': ['Unix'],
    'url': 'https://github.com/respect31/run',
    'long_description': '''.. Builded for run 0.8.1 from _templates/README.rst

Run
=====================
Run is library to provide common functionality.

.. image:: https://secure.travis-ci.org/respect31/run.png?branch=master 
     :target: https://travis-ci.org/respect31/run 
     :alt: build
.. image:: https://coveralls.io/repos/respect31/run/badge.png?branch=master 
     :target: https://coveralls.io/r/respect31/run  
     :alt: coverage
     
Quick Links
-----------
- `Package index (PyPi) <https://pypi.python.org/pypi?:action=display&name=runpack>`_
- `Source code (GitHub) <https://github.com/respect31/run>`_
- `Documentation (ReadTheDocs) <http://run.readthedocs.org/en/latest/>`_

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install runpack

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

if __name__ == '__main__':
    setup(**package)