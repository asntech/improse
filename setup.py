#!/usr/bin/env python

"""
This is a setup script for Improse -- Integrated Methods for Prediction of Super-Enhancers

This code is free software; you can redistribute it and/or modify it under the terms of the 
BSD License (see the file LICENSE.md included with the distribution).

@version: 1.0
@author: Aziz Khan
@email: khana10@mails.tsinghua.edu.cn
"""
import os
from distutils.core import setup
from setuptools import find_packages

#VERSION = __import__("improse").__version__

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
]

install_requires = [
    #'scipy',
    #'numpy',
    #'sklearn',
    #'pandas',
]

setup(
    name="improse",
    description="Integrated Methods for Prediction of Super-Enhancers",
    version=0.1,
    author="Aziz Khan",
    #Keywords= "bioinformatics,genomics",
    author_email="khana10@mails.tsinghua.edu.cn",
    url="https://github.com/asntech/improse",
    package_dir={'improse': 'improse'},
    packages=['improse'],
    scripts=['improse/improse',
                   ],
    package_data={'improse': ['improse/data/*.csv']},
    include_package_data=True,
    install_requires = install_requires,
    classifiers=CLASSIFIERS,
)
