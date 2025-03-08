from setuptools import setup, find_packages

setup(
    name="QGIS_Integration_Plugin",
    version="0.1.1",
    packages=find_packages(),
    author="Pietro Riccardo Comelli",
    author_email="comelli.pietro@gmail.com",
    description="Un plugin per importare file GeoJSON in NetBox.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: Italian",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
    ],
)

