from setuptools import setup, find_packages
import os

with open('README.md') as fp:
    readme = fp.read()

with open('LICENSE') as fp:
    license = fp.read()

long_description = 'block chain triangular arbitrage'
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name="triangular_arbitrage",

    version='0.0.1',

    description=readme,

    url='http://github.com/mervynlh/triangular_arbitrage',

    author='mervynlh',
    author_email='mervyn_lh@163.com',

    license=license,

    keywords='block chain triangular arbitrage',

    packages=find_packages(exclude=['triangular_arbitrage']),
)