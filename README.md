# Nessie Python SDK

[![Build Status](https://travis-ci.org/nessieisreal/nessie-python-sdk.svg?branch=master)](https://travis-ci.org/nessieisreal/nessie-python-sdk)

Provides Wrapper Functions for Nessie API

## Usage
TODO



## Overview


    Geolocation 
    
    Atm / Branch 

    (multiple accounts per customer)
    Customer    |---  Accounts
    
    Account     |------ Bill
                    |
                    --- Deposit
                    |
                    --- Loan
                    |
                    --- Purchase    --- Merchant
                    |
                    --- Transfer
                    |
                    --- Withdrawal


## Development Setup

Install python 3.6.2 or greater

Setup virtual python environment

    pip install pipenv
    pipenv install --dev

To add packages


More info about pipenv: http://python-docs.readthedocs.io/en/latest/dev/virtualenvs.html


To run test package

    pipenv run python ./src/atmRequests.py
    
To test locally

    python3 -m unittest
    pylint --disable=R,C nessie


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

    
