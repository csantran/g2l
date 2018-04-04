# coding: utf-8
"""
Setup scriptp for pg2l

You can instal pg2l with

python3 setup.py install

and run test with

python3 setup.py test

See:
https://github.com/csantran/pg2l
"""

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from distutils.version import StrictVersion
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# reading long_description from README.rst
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# execute nosetests with options defined in setup.cfg
# see http://fgimian.github.io/blog/2014/04/27/running-nose-tests-with-plugins-using-the-setuptools-test-command/
class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
        pass

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests'])
        pass

    pass

# setup
setup(
    name='pg2l',
    version='0.1.dev1',
    description='Python package for define parametric L-systems that manipulate graphs',
    long_description=long_description,
    url='https://github.com/csantran/pg2l',
    author='Cédric Santran',
    author_email='santrancedric@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Artificial Life',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Interpreters',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='parametric l-system graph grammar interpreter',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=['networkx>=2'],  # Optional
    python_requires='>=3',

    cmdclass={'test': NoseTestCommand},
    # test_suite='nose.collector',
    tests_require=['nose'],
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    # extras_require={  # Optional
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # # If there are data files included in your packages that need to be
    # # installed, specify them here.
    # #
    # # If using Python 2.6 or earlier, then these have to be included in
    # # MANIFEST.in as well.
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # # Although 'package_data' is the preferred approach, in some case you may
    # # need to place data files outside of your packages. See:
    # # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # #
    # # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # # To provide executable scripts, use entry points in preference to the
    # # "scripts" keyword. Entry points provide cross-platform support and allow
    # # `pip` to create the appropriate form of executable for the target
    # # platform.
    # #
    # # For example, the following would provide a command called `sample` which
    # # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    # additional URLs
    project_urls={
        'Bug Reports': 'https://github.com/csantran/pg2l/issues',
        'Source': 'https://github.com/csantran/pg2l/',
    },
)
