import os
from setuptools import setup, find_packages

def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, "__init__.py")) as f:
        locals = {}
        exec(f.read(), locals)
        return locals["__version__"]

setup(
    name="ExtendedDiagramIcons",
    version=get_version(),
    author="Joshua Duma",
    author_email="joshua.duma@trader.ca",
    description="This is intended to be used in a project that uses the diagrams (diagrams as code) python package as an extention of the icons.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="",
    include_package_data=True,
    include=["resources/**/*"],
    repository="https://github.com/JoshuaDuma/ExtendedDiagramIcons",
    packages=find_packages(),
    install_requires=[
        "diagrams>=0.23.4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)