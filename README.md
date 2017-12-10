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

    // builds the tar file at dist/nessie-<version>.tar.gz stored in setup.py
    python setup.py sdist

    // uploads it to the test pip repo
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*


The account is **nessie**

Notes theres two separate pypi. A fake test at test.pypi.org and a real one.

For obvious reasons the password to the real pypi.org is not placed here.

To install it:

    pip install --index-url https://test.pypi.org/simple/ nessie

Testing on windows

    //Create new repo
    mkdir test-install-nessie
    cd test-install-nessie

    // create virtual environment
    python -m venv .

    // activate virtual environment
    Scripts\activate

    // install from test pip location
    pip install --index-url https://test.pypi.org/simple/ nessie

    
