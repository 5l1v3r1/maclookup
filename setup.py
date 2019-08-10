# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

REQUIRES = ["requests>=2.22.0","argparse","regex"]
setup(
    name='maclookup',
    version='1.0',
    description="MAC address vendor lookup",
    keywords=["maclookup", "mac address"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A command-line utility to lookup info related to a MAC address 
    """
)
