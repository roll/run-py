import os
from setuptools import find_packages, setup

setup(

	#Main

    name='{{ run.name }}',
	version='{{ run.version }}',
	packages=find_packages(os.path.dirname(__file__) or '.', exclude=['tests*']),
	include_package_data=True,
    data_files=[('/etc/bash_completion.d', ['run/completion/run.sh'])],
    entry_points={'console_scripts': ['run = run:program']},
    install_requires=['packgram>=0.6', 'lib31>=0.6', 'jinja2>=2.7'],     
    tests_require=['nose'],
    test_suite='nose.collector',
    
    #Description
    
    author='{{ run.author }}',
    author_email='{{ run.author_email }}',
    maintainer='{{ run.maintainer }}',
    maintainer_email='{{ run.maintainer_email }}',
    license='{{ run.license }}',    
    url='https://github.com/{{ run.author|lower }}/{{ run.name|lower }}',
    download_url='https://github.com/{{ run.author|lower }}/{{ run.name|lower }}/tarball/{{ run.version|lower }}',    
    classifiers={{ run.classifiers }},    
    description='{{ run.description }}',    
    long_description='''{{ run.long_description }}''',
        
)