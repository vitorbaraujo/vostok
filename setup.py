import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kac-parser",
    version="0.0.2",
    author="vitorbaraujo",
    author_email="vitornga15@gmail.com",
    description="A python parser for Keep a Changelog changelog convention",
    long_description=long_description,
    url="https://github.com/vitorbaraujo/keep-a-changelog-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
