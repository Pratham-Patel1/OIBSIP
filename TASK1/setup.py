"""
Setup configuration for Iris Classification project.

This setup file allows the project to be installed as a package for easier
distribution and dependency management.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="iris-classification",
    version="1.0.0",
    author="OASIS INFOBYTE",
    author_email="info@oasisinfobyte.com",
    description="Iris Flower Classification using Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oasisinfobyte/iris-classification",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
        "joblib>=1.0.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
    ],
    extras_require={
        "dev": [
            "jupyter>=1.0.0",
            "ipython>=7.0.0",
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
        ],
    },
)
