#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()


setup(name='redflyingbaron',
      version='0.1.1',
      description='Project wrapper arround RedBaron',
      author='Laurent Peuch',
      long_description=read_md("README.md") + "\n\n" + open("CHANGELOG", "r").read(),
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
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                   'Topic :: Software Development',
                   'Topic :: Software Development :: Code Generators',
                  ]
     )
