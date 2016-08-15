#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='template_korean',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'django',
        'korean',
    ]
)
