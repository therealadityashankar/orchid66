import setuptools

with open("README.md") as f:
    README = f.read()

setuptools.setup(
    name="orchid66",
    version="1.1.6",
    description="print in color easily!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/therealadityashankar/orchid66",
    author="Aditya Shankar",
    author_email="aditniru@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    py_modules=["orchid66", "x11_colors"]
)
