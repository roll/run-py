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
	'data_files': [('/etc/bash_completion.d', ['data/run.sh'])],
    'entry_points': {'console_scripts': ['run = run:program']},
    'install_requires': ['box>=0.8', 'jinja2>=2.7'],  
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': '{{ author }}',
    'author_email': '{{ author_email }}',
    'maintainer': '{{ maintainer }}',
    'maintainer_email': '{{ maintainer_email }}',
    'license': '{{ license }}',    
    'url': 'https://github.com/{{ github_user }}/{{ name }}',
    'download_url':'https://github.com/{{ github_user }}/{{ name }}/tarball/{{ version }}',    
    'classifiers': {{ classifiers }},    
    'description': '{{ description }}',    
    'long_description': '''{{ long_description }}''',
    
}

if __name__ == '__main__':
    setup(**package)