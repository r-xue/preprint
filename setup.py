#!/usr/bin/env python

PROJECT = 'preprint'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages, Command

# from setuptools.core import setup, Command
# you can also import from setuptools


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''


setup(
    name=PROJECT,
    version=VERSION,

    description='Tools for writing latex papers',
    long_description=long_description,

    author='Jonathan Sick',
    author_email='jonathansick@mac.com',

    url='https://github.com/jonathansick/preprint',
    download_url='',

    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff', 'watchdog', 'GitPython', 'pytest'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    cmdclass={'test': PyTest},

    entry_points={
        'console_scripts': [
            'preprint = preprint.main:main'
        ],
        'preprint.commands': [
            'make = preprint.make:Make',
            'watch = preprint.watch:Watch',
            'diff = preprint.latexdiff:Diff',
            'pack = preprint.pack:Package',
        ],
    },

    zip_safe=False,
)
