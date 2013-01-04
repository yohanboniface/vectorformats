#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

classifiers = [
               'Development Status :: 4 - Beta',
               'Intended Audience :: Developers',
               'Intended Audience :: Science/Research',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Scientific/Engineering :: GIS',
               ]

setup(name='vectorformats',
      version='0.2',
      description='geographic data serialization/deserialization library',
      long_description=read('doc/Readme.txt'),
      author='FeatureServer (iocast)',
      author_email='featureserver@live.com',
      url='http://featureserver.org/vectorformats.html',
      install_requires=['dxfwrite>=1.2.0',
                        'pyspatialite>=3.0.1'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      license="MIT",
      classifiers=classifiers
)
