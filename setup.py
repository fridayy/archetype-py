#!/usr/bin/env python
from setuptools import setup, find_packages

# dependencies
install_requires = []
extras_require = {}

VERSION = '0.0.0'

setup(name='archetype-py',
      version=VERSION,
      description="tbd",
      long_description="tbd",
      author='Your Name',
      author_email='Your Mail',
      url='www.leftshift.one',
      license='proprietary',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'tests.*', 'release']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require=extras_require,
      # change me!
      entry_points={'console_scripts': [
          'archetype = archetype:main']})
