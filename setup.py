from setuptools import setup, find_packages
import os
import requests


# 将markdown格式转换为rst格式
def md_to_rst(from_file, to_file):
    r = requests.post(url='http://c.docverter.com/convert',
                      data={'to': 'rst', 'from': 'markdown'},
                      files={'input_files[]': open(from_file, 'rb')})
    if r.ok:
        with open(to_file, "wb") as f:
            f.write(r.content)

md_to_rst("README.md", "README.rst")

long_description = 'block chain triangular arbitrage'
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name="triangular_arbitrage",

    version='0.1.2',

    description='block chain triangular arbitrage',

    url='http://github.com/mervynlh/triangular_arbitrage',

    author='mervynlh',
    author_email='mervyn_lh@163.com',

    license='MIT',

    keywords='block chain triangular arbitrage',

    packages=find_packages(exclude=['triangular_arbitrage']),
)