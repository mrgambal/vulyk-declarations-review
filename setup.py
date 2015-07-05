#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pip.req import parse_requirements

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())

requirements = [str(ir.req) for ir in install_reqs]
test_requirements = requirements


setup(
    name='vulyk_declarations_review',
    version='0.1.0',
    description="Vulyk processed declarations review plugin",
    long_description=readme + '\n\n' + history,
    author='Dmytro Hambal',
    author_email='mr_gambal@outlook.com',
    url='https://github.com/mrgambal/vulyk-declarations-review',
    packages=[
        'vulyk_declarations_review',
        'vulyk_declarations_review.models',
        'vulyk_declarations_review.static',
        'vulyk_declarations_review.views'
    ],
    package_dir={'vulyk_declarations_review':
                 'vulyk_declarations_review'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='vulyk_declarations_review',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    scripts=[],
    tests_require=test_requirements
)
