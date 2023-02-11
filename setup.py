from setuptools import find_packages
from setuptools import setup

__version__ = "0.1"

setup(
    name="src",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "flask",
        "flask-restful",
        "flask-jwt-extended",
        "flask-marshmallow",
        "python-dotenv",
        "passlib",
        "apispec[yaml]",
        "apispec-webframeworks",
    ]
)
