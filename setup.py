# -*- coding: utf-8 -*-

from setuptools import setup
import warnings

README = 'README.md'
name = 'nx2tikz'

try:
    long_description = open('README.md').read()
except:
    warnings.warn('Could not find {readme}'.format(readme=README))

setup(
    name=name,
    version='0.1',
    license='BSD',
    description='Export NetworkX graphs to TikZ.',
    long_description=long_description,
    author='Ioannis Filippidis',
    author_email='jfilippidis@gmail.com',
    url = 'https://github.com/johnyf/nx2tikz',
    install_requires=['networkx'],
    packages=[name],
    package_dir={name: name},
    keywords = ['tikz', 'pgf', 'networkx', 'tex', 'latex', 'graph'],
    classifiers = [],
)
