from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="evntaly_python",
    version="1.0.13",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["requests"],
    description="A Python SDK for Evntaly event tracking platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alameer Ashraf",
    author_email="alameer@evntaly.com",
    url="https://github.com/Evntaly/evntaly-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)