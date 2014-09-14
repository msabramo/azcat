from setuptools import setup, find_packages

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="azcat",
    version="0.41",
    description="A alternative to cat(1); specialized for printing files",
    long_description=long_description,
    author="Seiya Nuta",
    author_email="nuta@seiya.me",
    url="http://github.com/ntsy/azcat",
    packages=["azcat"],
    scripts=["az"],
    install_requires=["pygments", "colorama", "BeautifulSoup4", "prettytable"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: Public Domain",
        "Operating System :: POSIX",
        "Topic :: Utilities"
    ]
)
