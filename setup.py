from setuptools import setup, find_packages

setup(
    name="basicrpg",
    version="0.0.8",
    description="Python library for making RPG games, clean and easy.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Unlisted_dev",
    #author_email="your_email@example.com",
    url="https://github.com/Unlisted27/basicrpg",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
