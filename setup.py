try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='beancount-cryptoassets',
    version='1.0.0',
    description='Beancount Cryptoassets',
    packages=['beancount_cryptoassets'],
    license='GPLv3',
)