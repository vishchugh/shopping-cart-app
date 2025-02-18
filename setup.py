from setuptools import setup, find_packages

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name="shopping_cart",
    version="1.0",
    packages=find_packages(include=["shopping_cart", "shopping_cart.*"]),
    install_requires=REQUIREMENTS
)
