import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vostok",
    version="0.0.3",
    author="vitorbaraujo",
    author_email="vitornga15@gmail.com",
    description="A chagelog parser for Keep a Changelog format",
    long_description=long_description,
    url="https://github.com/vitorbaraujo/vostok",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
