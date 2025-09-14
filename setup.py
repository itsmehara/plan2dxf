from setuptools import setup, find_packages

setup(
    name="plan2dxf",
    version="0.1.0",
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