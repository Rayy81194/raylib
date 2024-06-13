from setuptools import setup, find_packages

setup(
    name='raylib',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests', 'websocket-client', 'httpx[http2]', 'httpx'],)
    ],
)

