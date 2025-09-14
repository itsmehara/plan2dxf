from setuptools import setup, find_packages

with open("VERSION.txt") as verFP:
    VERSION = verFP.read().strip()

setup(
    name="plan2dxf",
    version=VERSION,
    description="Convert floor plan sketches/images/dimensions into AutoCAD DXF files.",
    packages=find_packages(exclude=("tests", "examples")),
    include_package_data=True,
    install_requires=[
        "ezdxf>=1.0",
    ],
    author="Hara",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)