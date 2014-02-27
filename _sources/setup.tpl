#Builded for {{ name }} {{ version }} from _templates/setup.tpl

import os
from setuptools import find_packages, setup

package = {

	#Main

    'name': '{{ pypi_name }}',
	'version':'{{ version }}',
	'packages': find_packages(
        os.path.dirname(__file__) or '.', 
        exclude=['tests*']
    ),
	'include_package_data': True,
    'install_requires': {{ install_requires }},  
    'tests_require': {{ tests_require }},
    'test_suite': '{{ test_suite }}',
    
    #Description
    
    'author': '{{ author }}',
    'author_email': '{{ author_email }}',
    'classifiers': {{ classifiers }},       
    'description': '{{ description }}',
    'download_url':'https://github.com/{{ github_user }}/{{ name }}/tarball/{{ version }}',
    'license': '{{ license }}',
    'maintainer': '{{ maintainer }}',
    'maintainer_email': '{{ maintainer_email }}',
    'platforms': {{ platforms }},
    'url': 'https://github.com/{{ github_user }}/{{ name }}',
    'long_description': '''{{ long_description }}''',  
    
}

if (not os.environ.get('TRAVIS', None) and  
	not	os.environ.get('READTHEDOCS', None)):
	package['entry_points'] = {'console_scripts': ['run = run:program']}
	package['data_files'] = [('/etc/bash_completion.d', ['data/run.sh'])]	

if __name__ == '__main__':
	setup(**package)