""" lambdata - a collection of Data Science helper functions
"""
import setuptools

REQUIRED = [
    "numpy",
    "pandas",
    "scipy"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata-Tristan-Brown1096",
    version="0.0.5",
    author="Tristan-Brown1096",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content="text/markdown",
    url="https://github.com/Tristan-Brown1096/lambdata",
    package=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)