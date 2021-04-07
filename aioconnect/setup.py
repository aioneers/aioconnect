import setuptools
from setuptools import setup
from pathlib import Path
import os
import platform

# Make the Readme.md as long description
# if platform.system() == "Linux":
#     long_description = "not yet working on Databricks"
# else:
#     with open(
#         str(Path(os.path.abspath(__file__)).parent.parent) + "/README.md", "r"
#     ) as fh:
#         long_description = fh.read()

long_description = "not yet working"

setuptools.setup(
    name="aioconnect",
    version="0.0.2",
    author="AIO",
    author_email="maintainer@aioneers.com",
    license="MIT",
    description="AIO connect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aioneers/aioconnect",
    download_url="https://github.com/aioneers/aioconnect/archive/0.0.2.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "aio@git+https://github.com/aioneers/aio.git#subdirectory=aio",
        "pytest",
        "pydata_sphinx_theme",
        "nbsphinx",
        "numpydoc",
        "pandas",
        "requests",
        "datetime",
        "azure-keyvault",
        "azure-identity",
    ],
)
