#!/usr/bin/env python

from setuptools import find_packages
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='my-package',
      version='0.0.1',
      description='My Package Test Case',
      author='Vitor Barbosa',
      author_email='vitorpbarbosa7@email.com',
      packages=[find_packages()]
     )
