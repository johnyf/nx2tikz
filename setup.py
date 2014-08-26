# -*- coding: utf-8 -*-

import os
from setuptools import setup

if os.path.exists('README.txt'):
    long_description = open('README.txt').read()
elif os.path.exists('README.md'):
    long_description=open('README.md').read()
else:
    print('Could not find readme from which to extract long_description.')
    long_description = ''

setup(
    name='nx2tikz',
    version='0.1',
    py_modules=['nx2tikz'],
    license='BSD',
    description='Export NetworkX graphs to TikZ.',
    long_description=long_description,
    author='Ioannis Filippidis',
    author_email='jfilippidis@gmail.com',
    url = 'https://github.com/johnyf/nx2tikz',
    #download_url = 'https://github.com/johnyf/pycflow2dot/archive/v0.2.tar.gz',
    install_requires=['networkx'],
    keywords = ['tikz', 'pgf', 'networkx', 'tex', 'latex', 'graph',
                'dot'],
    classifiers = [],
)
