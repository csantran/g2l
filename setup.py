"""
Setup scriptp for g2l

You can instal g2l with

python3 setup.py install

See:
https://github.com/csantran/g2l
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='g2l',
    version='0.0.dev1',
    description='Python package for define parametric L-systems that manipulate graphs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/csantran/g2l',
    author='Santran Cédric',
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='parametric l-system graph grammar interpreter',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=['networkx>=2'],  # Optional

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

    # # List additional URLs that are relevant to your project as a dict.
    # #
    # # This field corresponds to the "Project-URL" metadata fields:
    # # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    # #
    # # Examples listed include a pattern for specifying where the package tracks
    # # issues, where the source is hosted, where to say thanks to the package
    # # maintainers, and where to support the project financially. The key is
    # # what's used to render the link text on PyPI.
    # project_urls={  # Optional
    #     'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #     'Funding': 'https://donate.pypi.org',
    #     'Say Thanks!': 'http://saythanks.io/to/example',
    #     'Source': 'https://github.com/pypa/sampleproject/',
    # },
)
