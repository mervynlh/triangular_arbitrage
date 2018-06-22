from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="triangular_arbitrage",

    version='0.1',

    description='block chain triangular arbitrage',

    url='http://github.com/mervynlh/triangular_arbitrage',

    author='mervynlh',
    author_email='mervyn_lh@163.com',

    license='MIT',

    keywords='block chain triangular arbitrage',

    packages=find_packages(exclude=['triangular_arbitrage']),
)