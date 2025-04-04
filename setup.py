# so this will maek the package installable

from setuptools import setup, find_packages

setup(
    name="switchmap-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pysnmp>=4.4.12",
        "pyzmq>=24.0.0",
        "aiohttp>=3.8.1",
        "pyyaml>=6.0",
        "sqlalchemy>=1.4.0",
    ],
    author="Abhishek Raj",
    author_email="abhishek4code@gmail.com",
    description="Core module for SwitchMap-NG",
    keywords="network, snmp, monitoring",
)