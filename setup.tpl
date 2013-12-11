import os
from setuptools import find_packages, setup

package = {

	#Main

    'name': '{{ name }}',
	'version': '{{ version }}',
	'packages': find_packages(os.path.dirname(__file__) or '.', exclude=['tests*']),
	'include_package_data': True,
    'data_files': [
        ('/etc/bash_completion.d', ['run/completion/run.sh'])       
    ],
    'entry_points': {
        'console_scripts': [
            'run = run:program',
        ]
    },
    'install_requires': ['packgram>=0.6', 'lib31>=0.6'],     
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': '{{ author }}',
    'author_email': '{{ author_email }}',
    'maintainer': '{{ maintainer }}',
    'maintainer_email': '{{ maintainer_email }}',
    'license': '{{ license }}',    
    'url': 'https://github.com/{{ author|lower }}/{{ name|lower }}',
    'download_url': 'https://github.com/{{ author|lower }}/{{ name|lower }}/tarball/{{ version|lower }}',    
    'classifiers': {{ classifiers }},    
    'description': '{{ description }}',    
    'long_description': '''{{ long_description }}''',
        
}

if __name__ == '__main__':
    setup(**package)