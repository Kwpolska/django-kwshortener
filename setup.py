#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from setuptools import setup

with open('requirements.txt', 'r') as fh:
    dependencies = [l.strip() for l in fh]

setup(name='django-kwshortener',
      version='0.1.1',
      description='Yet another URL shortener',
      keywords='django,url,shortener',
      author='Chris Warrick',
      author_email='chris@chriswarrick.com',
      url='https://github.com/Kwpolska/django-kwshortener',
      license='3-clause BSD',
      long_description=io.open('./README.rst', 'r', encoding='utf-8').read(),
      platforms='any',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 2 - Alpha',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3'],
      packages=['kwshortener'],
      install_requires=dependencies,
      #requires=['stuff'],
      #data_files=[('file', ['dest']),],
      #entry_points={
          #'console_scripts': [
              #'template = tEmplate.__main__:main',
          #]
      #},
      )
