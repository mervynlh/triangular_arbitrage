from setuptools import setup, find_packages
import os
import requests


with open('README.rst') as fp:
    readme = fp.read()

with open('LICENSE') as fp:
    license = fp.read()

long_description = 'block chain triangular arbitrage'
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name="triangular_arbitrage",

    version='0.1.3',

    description=readme,

    url='http://github.com/mervynlh/triangular_arbitrage',

    author='mervynlh',
    author_email='mervyn_lh@163.com',

    license=license,

    keywords='block chain triangular arbitrage',

    packages=find_packages(exclude=['triangular_arbitrage']),
)