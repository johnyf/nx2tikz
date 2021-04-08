"""Installation script."""
from setuptools import setup
import warnings


README = 'README.md'
name = 'nx2tikz'
try:
    long_description = open('README.md').read()
except:
    warnings.warn('Could not find {readme}'.format(readme=README))
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


if __name__ == '__main__':
    setup(
        name=name,
        version='0.2.0',
        license='BSD',
        description='Export NetworkX graphs to TikZ.',
        long_description=long_description,
        author='Ioannis Filippidis',
        author_email='jfilippidis@gmail.com',
        url='https://github.com/johnyf/nx2tikz',
        install_requires=['networkx'],
        packages=[name],
        package_dir={name: name},
        entry_points={
            'console_scripts':
                ['nx2tikz = nx2tikz.nx2tikz:command_line']},
        keywords=[
            'tikz', 'pgf', 'networkx', 'tex', 'latex', 'luatex',
            'lualatex', 'graph'],
        classifiers=classifiers)
