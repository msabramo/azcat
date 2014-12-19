from setuptools import setup, find_packages

requires = open("requirements.txt").read().split("\n")
readme = open("README.rst").read()

setup(
    name="azcat",
    version="0.60",
    description="A alternative to cat(1); specialized for printing files",
    long_description=readme,
    author="Seiya Nuta",
    author_email="nuta@seiya.me",
    url="http://github.com/nuta/azcat",
    packages=find_packages(),
    scripts=["az"],
    install_requires=requires,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: Public Domain",
        "Operating System :: POSIX",
        "Topic :: Utilities"
    ]
)
