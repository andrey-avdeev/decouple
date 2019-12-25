# -*- coding: utf-8 -*-
import io

from setuptools import setup, find_packages

with io.open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

version = "0.0.7"

setup(
    name="decouple",
    version=version,
    description="Decoupling logic",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Andrey Avdeev",
    author_email="seorazer@gmail.com",
    license="Apache 2.0",
    packages=["decouple"],
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[],
    keywords="decouple mediator decoupling",
    url="https://github.com/andrey-avdeev/decouple",
)
