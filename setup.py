#!/usr/bin/env python

from setuptools import setup

setup(
    name="serializer",
    version="1.0.0",
    description="Module allowing to serialize and deserialize objects",
    author="Polina Zorko",
    author_email='kzhibul@gmail.com',
    url="https://github.com/karoliys/ISP4sem",
    setup_requires=["wheel"],
    install_requires=["pyyaml", "wheel", "toml"],
    packages=["ser_create/", "."],
    entry_points={"console_scripts": "cu=console_util:main"},
)
