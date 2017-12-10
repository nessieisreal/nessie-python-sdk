# Nessie Python SDK
Provides Wrapper Functions for Nessie API

## Usage
TODO


## Development Setup

Install python 3.6.2 or greater

Setup virtual python environment

    pip install pipenv
    pipenv install

To add packages


More info about pipenv: http://python-docs.readthedocs.io/en/latest/dev/virtualenvs.html


To run test package

    pipenv run python ./src/atmRequests.py


## Deploying to pip

https://packaging.python.org/tutorials/distributing-packages/
https://packaging.python.org/guides/using-testpypi/#using-test-pypi

Note make sure not to save the .pypirc file with the pip password lol


    python setup.py sdist


The account is **nessie**

Notes theres two separate pypi. A fake test at test.pypi.org and a real one.

For obvious reasons the password to the real pypi.org is not placed here.