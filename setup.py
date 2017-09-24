"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='serp',
    version='0.0.1',
    description='Stupid ERP is ERP middleware for your projects',
    long_description=long_description,
    url='https://github.com/devsli/serp',
    author='Leonid Suprun',
    author_email='leonid@suprun.pw',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Office/Business :: Groupware',
    ],
    keywords='simple stupid erp middleware',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['peewee'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
