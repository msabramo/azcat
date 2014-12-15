from setuptools import setup, find_packages

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="azcat",
    version="0.60",
    description="A alternative to cat(1); specialized for printing files",
    long_description=long_description,
    author="Seiya Nuta",
    author_email="nuta@seiya.me",
    url="http://github.com/nuta/azcat",
    packages=find_packages(),
    scripts=["az"],
    install_requires=["pygments", "colorama", "BeautifulSoup4", "prettytable",
                      "python-magic", "chardet"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: Public Domain",
        "Operating System :: POSIX",
        "Topic :: Utilities"
    ]
)
