from setuptools import find_packages, setup

with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="kfc",
    version="0.1.0",
    description="Data sicence with tf feature columns",
    long_description=readme,
    author="Tiep Vu",
    author_email="vuhuutiep@gmail.com",
    url="https://github.com/tiepvupsu/kfcd",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
