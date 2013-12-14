import os
from setuptools import find_packages, setup

setup(

	#Main

    name='None',
	version='',
	packages=find_packages(os.path.dirname(__file__) or '.', exclude=['tests*']),
	include_package_data=True,
    data_files=[('/etc/bash_completion.d', ['run/completion/run.sh'])],
    entry_points={'console_scripts': ['run = run:program']},
    install_requires=['packgram>=0.6', 'lib31>=0.6', 'jinja2>=2.7'],     
    tests_require=['nose'],
    test_suite='nose.collector',
    
    #Description
    
    author='',
    author_email='',
    maintainer='',
    maintainer_email='',
    license='',    
    url='https://github.com//none',
    download_url='https://github.com//none/tarball/',    
    classifiers=,    
    description='',    
    long_description='''''',
        
)