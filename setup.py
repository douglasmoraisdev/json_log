import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json_log",
    version="0.0.1",
    author="Douglas Morais",
    author_email="msantos.douglas@gmail.com",
    description="Logs on JSON format, for general purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/douglasmoraisdev/json_log",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)