"""Installation script."""
import os

from setuptools import setup
import warnings


README = 'README.md'
NAME = 'nx2tikz'
DESCRIPTION = 'Export NetworkX graphs to TikZ.'
url = f'https://github.com/johnyf/{NAME}'
VERSION_FILE = f'{NAME}/_version.py'
MAJOR = 0
MINOR = 2
MICRO = 0
VERSION = f'{MAJOR}.{MINOR}.{MICRO}'
VERSION_TEXT = (
    '# This file was generated from setup.py\n'
    "version = '{version}'\n")
PYTHON_REQUIRES = '>=3.9'
INSTALL_REQUIRES = ['networkx']
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Multimedia :: Graphics',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Text Processing :: Markup :: LaTeX']


def run_setup():
    s = VERSION_TEXT.format(version=VERSION)
    with open(VERSION_FILE, 'w') as f:
        f.write(s)
    long_description = _long_description()
    setup(
        name=NAME,
        version=VERSION,
        license='BSD',
        description=DESCRIPTION,
        long_description=long_description,
        author='Ioannis Filippidis',
        author_email='jfilippidis@gmail.com',
        url=url,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        packages=[NAME],
        package_dir={NAME: NAME},
        entry_points={
            'console_scripts':
                ['nx2tikz = nx2tikz.nx2tikz:command_line']},
        keywords=[
            'tikz', 'pgf', 'networkx', 'tex', 'latex', 'luatex',
            'lualatex', 'graph'],
        classifiers=CLASSIFIERS)


def _long_description():
    """Return contents of README file."""
    if not os.path.isfile(README):
        warnings.warn(
            f'Did not find file `{README}`')
        return ''
    with open(README) as f:
        return f.read()


if __name__ == '__main__':
    run_setup()
