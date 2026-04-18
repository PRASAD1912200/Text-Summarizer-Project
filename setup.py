from setuptools import setup, find_packages

setup(
    name="textSummarizer",
    version="0.0.1",
    author="Prasad",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)