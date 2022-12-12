# flake8: noqa
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pinocchio",
    version="0.0.1",
    author="Albert Li",
    author_email="alberthli@caltech.edu",
    description="Pinocchio fork, Dec 11, 2022.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alberthli/pinocchio-frozen",
    packages=setuptools.find_packages(
        where="./bindings/python/pinocchio",
        include=["pinocchio"],
    ),
    package_dir={"": "bindings/python/pinocchio"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.10",
    license="MIT",
    # install_requires=[
    #     "numpy",
    # ],
)
