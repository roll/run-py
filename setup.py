import os
from setuptools import find_packages, setup

setup(

	#Main

    name='runpack',
	version='0.8.1',
	packages=find_packages(os.path.dirname(__file__) or '.', exclude=['tests*']),
	include_package_data=True,
    data_files=[('/etc/bash_completion.d', ['data/run.sh'])],
    entry_points={'console_scripts': ['run = run:program']},
    install_requires=['lib31>=0.7', 'jinja2>=2.7'],     
    tests_require=['nose'],
    test_suite='nose.collector',
    
    #Description
    
    author='Respect31',
    author_email='post@respect31.com',
    maintainer='Respect31',
    maintainer_email='post@respect31.com',
    license='MIT License',    
    url='https://github.com/respect31/runpack',
    download_url='https://github.com/respect31/runpack/tarball/0.8.1',    
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: System :: Systems Administration'],    
    description='Run is program to run tasks from files.',    
    long_description='''Run
===
Run is program to run tasks from files.

.. image:: https://secure.travis-ci.org/respect31/run.png?branch=master 
     :target: https://travis-ci.org/respect31/run
     :alt: build
.. image:: https://coveralls.io/repos/respect31/run/badge.png?branch=master 
     :target: https://coveralls.io/r/respect31/run  
     :alt: coverage
.. image:: https://badge.fury.io/py/runpack.png
     :target: http://badge.fury.io/py/runpack
     :alt: index

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install runpack

Classifiers
-----------
- Development Status :: 3 - Alpha
- Intended Audience :: Developers
- License :: OSI Approved :: MIT License
- Programming Language :: Python :: 3.3
- Topic :: Software Development :: Libraries :: Python Modules
- Topic :: System :: Systems Administration

History
-------
0.8.0
`````
- changed concept to build tool''',
        
)