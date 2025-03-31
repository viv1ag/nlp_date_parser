from setuptools import setup, find_packages

setup(
    name="nlp_date_parser",
    version="0.0.2",
    author="Vivek Agarwal",
    author_email="ec.vivek@gmail.com",
    description="A natural language date parser for Python.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/viv1ag/nlp_date_parser",
    packages=setuptools.find_packages(),
    install_requires=[
        "python-dateutil",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
