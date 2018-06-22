from setuptools import setup, find_packages

with open('README.md') as fp:
    readme = fp.read()

with open('LICENSE') as fp:
    license = fp.read()

setup(
    name="triangular_arbitrage",

    version='0.0.1',

    description='block chain triangular arbitrage',

    long_description=readme,

    url='http://github.com/mervynlh/triangular_arbitrage',

    author='mervynlh',

    author_email='mervyn_lh@163.com',

    license=license,

    keywords='block chain triangular arbitrage',

    packages=find_packages(exclude=['triangular_arbitrage']),
)