from setuptools import setup, find_packages

setup(
    name='raylib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'httpx',
        'websocket-client',
        'requests',
        'httpx[http2]'
    ],
)

