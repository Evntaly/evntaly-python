from setuptools import setup, find_packages

setup(
    name="evntaly-python",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests"],
    description="A Python SDK for Evntaly event tracking platform",
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