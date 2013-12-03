import os
from setuptools import find_packages, setup

package = {

	#Main

    'name': 'runpack',
	'version': '0.7.1',
	'packages': find_packages(os.path.dirname(__file__), exclude=['tests*']),
	'include_package_data': True,
    'data_files': [
        ('/etc/bash_completion.d', ['run/completion/run.sh'])       
    ],
    'entry_points': {
        'console_scripts': [
            'run = run:program',
        ]
    },
    'install_requires': ['packgram>=0.5', 'ipclight>=0.5'],     
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': 'Respect31',
    'author_email': 'post@respect31.com',
    'maintainer': 'Respect31',
    'maintainer_email': 'post@respect31.com',
    'license': 'MIT License',    
    'url': 'https://github.com/respect31/runpack',
    'download_url': 'https://github.com/respect31/runpack/tarball/0.7.1',    
    'classifiers': ['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: System :: Systems Administration'],    
    'description': 'Program to run methods from file.',    
    'long_description': '''Run
===
Program to run methods from file.

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install runpack

Example
-------
- create runfile.py in current working directory::

    from run import Run

    class Run(Run):
    
        #Public
    
        def hello(self, person, times=1):
            """Print 'Hello {person} {times} times!'"""
            print('Hello {person} {times} times!'.format(person=person,
                                                         times=str(times)))
            
- get methods list from command line::

    $ run
    hello
    help
    list

- autocomplete method from command line::

    $ run he<TAB>
    $ run hello
    
- get method help from command line::

    $ run hello -h
    hello(person, times=1)
    Print 'Hello, {person}, {times} times!'

- run method from command line::

    $ run hello world, times=3
    Hello world 3 times!

History
-------
0.7.0
`````
- rewritten using IPC.Light
- moved to Python 3.3

0.6.0
`````
- included python driver

0.5.0
`````
- added user settings

0.4.0
`````
- added autocompletion

0.3.0
`````
- added runclass methods running
- added runfile running by absolute path
- renamed option filename to runfile

0.2.0
`````
- added driver seeking in current working directory''',
        
}

if __name__ == '__main__':
    setup(**package)