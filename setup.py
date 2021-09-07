"""Installation script."""
from setuptools import setup
import warnings


README = 'README.md'
NAME = 'nx2tikz'
DESCRIPTION = 'Export NetworkX graphs to TikZ.'
try:
    with open('README.md') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''
    warnings.warn('Could not find {readme}'.format(readme=README))
url = f'https://github.com/johnyf/{NAME}'
VERSION_FILE = f'{NAME}/_version.py'
MAJOR = 0
MINOR = 2
MICRO = 0
VERSION = '{major}.{minor}.{micro}'.format(
    major=MAJOR, minor=MINOR, micro=MICRO)
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
    'Topic :: Multimedia :: Graphics',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Text Processing :: Markup :: LaTeX']


def run_setup():
    s = VERSION_TEXT.format(version=VERSION)
    with open(VERSION_FILE, 'w') as f:
        f.write(s)
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


if __name__ == '__main__':
    run_setup()
