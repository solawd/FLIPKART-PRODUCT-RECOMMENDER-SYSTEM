from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="FLIPKART RECOMMENDER",
    version="0.11",
    author="solawd",
    packages=find_packages(),
    install_requires = requirements,
)