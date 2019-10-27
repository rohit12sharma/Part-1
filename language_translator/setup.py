import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="language_package-Rohit",
    version="0.0.1",
    author="Rohit Sharma",
    author_email="rohit.sharma@iiitb.net",
    description="A Rule-based Text/Abbreviation conversion package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    install_requires=['re', 'csv'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
