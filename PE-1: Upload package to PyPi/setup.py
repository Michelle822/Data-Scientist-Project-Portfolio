# This file is needed by Python's setuptools for local installation from the pypi.org index (pip install linalg_simple)

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="algebra_easy",
    version="0.0.3",
    author="Michelle Leemans",
    author_email="michelleleemans91@gmail.com",
    description="Simple Linear Algebra Package",
    packages=['algebra_easy'],
    python_requires=">=3.6",
    zip_safe=False,
)
