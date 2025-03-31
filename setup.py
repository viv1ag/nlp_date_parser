from setuptools import setup, find_packages

setup(
    name="nlp_date_parser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "dateparser"  # If your package depends on it
    ],
    author="Vivek Agarwal",
    author_email="ec.vivek@gmail.com",
    description="A natural language date parser for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/viv1ag/nlp_date_parser",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
