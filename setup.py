#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Distribution setup module."""

__requires__ = ('setuptools >=41.0.0', )
# The list of pre-requisite requirements, needed to run this module

from setuptools import setup

setup_params = {
    'use_scm_version': True,
    'setup_requires': [
        'setuptools_scm>=3.3',
    ]
}

__name__ == '__main__' and setup(**setup_params)
