#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='TeensyCli',
    version='0.1.0',
    author='Marcell Vazquez-Chanlatte, William Kennington III',
    author_email='mvc@linux.com',
    packages=find_packages(),
    url='',
    license='LICENSE.txt',
    description='',
    long_description=open('README.org').read(),
    requires = [],
    entry_points={
        'console_scripts': [
            'pass2 = teensy_pass.main:main',
        ]
    }
)
