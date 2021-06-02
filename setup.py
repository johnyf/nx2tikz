"""Installation script."""
from setuptools import setup
import warnings


README = 'README.md'
name = 'nx2tikz'
description = 'Export NetworkX graphs to TikZ.'
try:
    with open('README.md') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''
    warnings.warn('Could not find {readme}'.format(readme=README))
url = 'https://github.com/johnyf/{name}'.format(name=name)
VERSION_FILE = '{name}/_version.py'.format(name=name)
MAJOR = 0
MINOR = 2
MICRO = 0
VERSION = '{major}.{minor}.{micro}'.format(
    major=MAJOR, minor=MINOR, micro=MICRO)
VERSION_TEXT = (
    '# This file was generated from setup.py\n'
    "version = '{version}'\n")
install_requires = ['networkx']
classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Multimedia :: Graphics',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Text Processing :: Markup :: LaTeX']


def run_setup():
    s = VERSION_TEXT.format(version=VERSION)
    with open(VERSION_FILE, 'w') as f:
        f.write(s)
    setup(
        name=name,
        version=VERSION,
        license='BSD',
        description=description,
        long_description=long_description,
        author='Ioannis Filippidis',
        author_email='jfilippidis@gmail.com',
        url=url,
        install_requires=install_requires,
        packages=[name],
        package_dir={name: name},
        entry_points={
            'console_scripts':
                ['nx2tikz = nx2tikz.nx2tikz:command_line']},
        keywords=[
            'tikz', 'pgf', 'networkx', 'tex', 'latex', 'luatex',
            'lualatex', 'graph'],
        classifiers=classifiers)


if __name__ == '__main__':
    run_setup()
