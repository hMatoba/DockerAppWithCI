
from setuptools import setup
import sys

sys.path.append('./tests')

setup(
    name = 'browsertest',
    version = '1.0',
    description = 'test a project on browser',
    test_suite = 'selenium_test.suite',
    test_require = [
        'selenium',
        'pymongo'
    ],
)