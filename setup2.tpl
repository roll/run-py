import os
from setuptools import find_packages, setup

setup(

	#Main

    name='{{ namespace.name }}',
	version='{{ namespace.version }}',
	packages=find_packages(os.path.dirname(__file__) or '.', exclude=['tests*']),
	include_package_data=True,
    data_files=[('/etc/bash_completion.d', ['run/completion/run.sh'])],
    entry_points={'console_scripts': ['run = run:program']},
    install_requires=['packgram>=0.6', 'lib31>=0.6', 'jinja2>=2.7'],     
    tests_require=['nose'],
    test_suite='nose.collector',
    
    #Description
    
    author='{{ namespace.author }}',
    author_email='{{ namespace.author_email }}',
    maintainer='{{ namespace.maintainer }}',
    maintainer_email='{{ namespace.maintainer_email }}',
    license='{{ namespace.license }}',    
    url='https://github.com/{{ namespace.author|lower }}/{{ namespace.name|lower }}',
    download_url='https://github.com/{{ namespace.author|lower }}/{{ namespace.name|lower }}/tarball/{{ namespace.version|lower }}',    
    classifiers={{ namespace.classifiers }},    
    description='{{ namespace.description }}',    
    long_description='''{{ namespace.long_description }}''',
        
)