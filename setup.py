from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="index_price_engine",
    version="0.0.1",
    description="Index Price Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bitwyre/derivatives_feed_engine",
    author="M Sidik Augi Rahmat",
    author_email="mohammedaugie@gmail.com",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="financial exchange cryptocurrency",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4",
    install_requires=[],  # Optional
    extras_require={"dev": ["check-manifest", "pycodestyle", "mypy", "pre-commit"], "test": ["coverage", "pytest"]},
    entry_points={"console_scripts": ["index_price_engine=index_price_engine:cli"]},
)
