"""Setup script for factorial-calculator package."""

from setuptools import find_packages, setup

setup(
    packages=find_packages(where="."),
    package_dir={"": "."},
)
