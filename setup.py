import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="sorted_iterators",
    version="0.0.1",
    author="Anatoly Scherbakov",
    author_email="altaisoft@gmail.com",
    description=(
        "Subtract or join iterators that are known to be sorted"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.org/anatoly.scherbakov/sorted-iterator-arithmetic',
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    extras_require={
        'dev': [
            'pytest'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)
