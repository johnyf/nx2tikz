# -*- coding: utf-8 -*-

from setuptools import setup
import warnings

README = 'README.md'

try:
    long_description = open('README.md').read()
except:
    warnings.warn('Could not find {readme}'.format(readme=README))

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
    install_requires=['networkx'],
    keywords = ['tikz', 'pgf', 'networkx', 'tex', 'latex', 'graph'],
    classifiers = [],
)
