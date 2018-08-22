try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Star',
    'url': 'https://github.com/chenstarsQ/',
    'download_url': 'https://github.com/chenstarsQ/',
    'author_email': 'Star (1140330611@qq.com)',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'lexicon.py'
}

setup(**config)
