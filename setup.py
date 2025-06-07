# setup.py
from setuptools import find_packages, setup

setup(
    name="fancy_logging",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tqdm==4.66.5",  # Ensure tqdm is installed for progress bars
    ],
    description="Beautiful, colorful, and configurable logging for Python.",
    author="Parth Patil",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
