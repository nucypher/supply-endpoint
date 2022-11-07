#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(name='nucypher-supply-information',
      version='1.0',
      description='NU token supply information server',
      author='nucypher',
      author_email='dev@nucypher.com',
      url='https://github.com/nucypher/supply-endpoint',
      packages=find_packages())

