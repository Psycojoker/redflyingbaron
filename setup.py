#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='redflyingbaron',
      version='0.1',
      description='Project wrapper arround RedBaron',
      author='Laurent Peuch',
      #long_description='',
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/redflyingbaron',
      install_requires=['baron>=0.6.1', 'redbaron>=0.5', 'ipython'],
      packages=[],
      py_modules=['redflyingbaron'],
      license= 'lGPLv3+',
      entry_points={
          'console_scripts': [
              'redflyingbaron = redflyingbaron:main',
              'red = redflyingbaron:main',
          ]
      },
      keywords='baron redbaron refactoring editor ast fst',
     )
