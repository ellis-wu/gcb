from setuptools import setup, find_packages
import sys

if sys.version_info <= (2, 7):
    error = "ERROR: gcb requires Python Version 2.7 or later...exiting."
    print(error)
    sys.exit(1)

requirements = [
    'google-api-python-client>=1.5.5',
]

setup(
    name='gcb',
    version='0.1.0',
    packages=find_packages(),
    description='Google Cloud Platform Ceph Backup Tools',
    author='Kyle Bai, Ellis Wu',
    author_email='kyle.b@inwinstack.com, ellis.w@inwinstack.com',
    url='https://github.com/kairen/gcb',
    install_requires=requirements,
    license="MIT",
    entry_points={})
