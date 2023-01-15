from pathlib import Path

from setuptools import find_namespace_packages, find_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]

style_packages = [
    "black==22.3.0",
    "isort==5.10.1",
    "mypy==0.910",
    "types-PyYAML==6.0.9",
    "types-pytz==2022.6.0.1",
    "types-requests==2.28.11.2",
    "types-simplejson==3.17.7.2",
]

test_packages = ["pytest==7.1.2", "great-expectations==0.15.42"]


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="python_project_template",
    version="0.1",
    description="Python project template",
    long_description=readme,
    author="vuhuutiep@gmail.com",
    author_email="",
    url="https://github.com/tiepvupsu/python_project_template",
    python_requires=">=3.8",
    license=license,
    packages=find_namespace_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[required_packages],
    extras_require={
        "dev": docs_packages + style_packages + test_packages + ["pre-commit==2.19.0"],
        "docs": docs_packages,
        "test": test_packages,
    },
)
