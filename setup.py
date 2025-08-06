"""Setup script for PyFtools package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyftools",
    version="0.1.0",
    author="PyFtools Contributors",
    author_email="brycewang@stanford.edu",
    description="Python implementation of ftools - Fast data manipulation tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brycewang-stanford/pyftools",
    project_urls={
        "Bug Tracker": "https://github.com/brycewang-stanford/pyftools/issues",
        "Documentation": "https://github.com/brycewang-stanford/pyftools",
        "Source Code": "https://github.com/brycewang-stanford/pyftools",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19.0",
        "pandas>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
            "sphinx",
            "sphinx-rtd-theme",
        ],
        "test": [
            "pytest>=6.0",
            "pytest-cov",
        ],
    },
    keywords="data manipulation, categorical variables, stata, ftools, statistics",
)
