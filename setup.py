try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os

setup(name='adsmsg',
      version='0.0.2',
      packages=['adsmsg', 'adsmsg.protobuf', 'adsmsg.tests'],
      install_requires=[
          'protobuf==3.3.0'
      ]
  )
