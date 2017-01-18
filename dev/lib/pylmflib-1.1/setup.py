#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import pylmflib

setup(name='pylmflib',
    version=pylmflib.wrapper.__version__,
    description='Python LMF library',
    long_description=open('README.rst').read(),
    author='Céline Buret',
    author_email='buret.celine@gmail.com',
    #install_requires=["docx", "odf"],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'Intended Audience :: End Users/Desktop',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Scientific/Engineering'],
    url='https://github.com/buret/pylmflib',
    py_modules=['pylmflib.wrapper'],
    packages=find_packages(),
    include_package_data=True,
)
