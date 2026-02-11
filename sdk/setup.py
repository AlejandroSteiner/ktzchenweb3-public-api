"""
KtzchenWeb3 Python SDK Setup
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ktzchenweb3",
    version="1.0.0",
    author="KtzchenWeb3",
    author_email="sdk@ktzchenweb3.io",
    description="Official Python SDK for the KtzchenWeb3 blockchain API platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ktzchenweb3/ktzchenweb3-public-api",
    project_urls={
        "Bug Tracker": "https://github.com/ktzchenweb3/ktzchenweb3-public-api/issues",
        "Documentation": "https://docs.ktzchenweb3.io",
        "Source": "https://github.com/ktzchenweb3/ktzchenweb3-public-api",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    py_modules=["ktzchenweb3"],
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "types-requests>=2.28.0",
        ],
    },
    keywords=[
        "web3",
        "blockchain",
        "ethereum",
        "polygon",
        "arbitrum",
        "bsc",
        "api",
        "sdk",
        "gas-fees",
        "smart-contracts",
        "defi",
        "crypto",
    ],
)
