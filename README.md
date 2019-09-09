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
## Development Setup

Install python 3.6.2 or greater

Setup virtual python environment

    pip install pipenv
    pipenv install

Since the stable version of this SDK is not pushed to the Python Package Index (PyPI), you will need to install it from this repository. Don't worry! You'll just need a few more `pip` commands and you'll be fine. Follow the steps below.

### Installation

First, clone this repository to somewhere you want to start your project, or where you'll remember where you cloned it.

```
$ git clone https://github.com/nessieisreal/nessie-python-sdk.git
```
Now we will package this project so you can import it elsewhere on your computer:
```
$ python3 -m pip install -e ./nessie-python-sdk/
```
Now, normally you would simply do `$ pip install nessie`, but since this project
 is not on PyPI yet, we cant directly do that. We have to tell pip to use a local
 project and use that as a package, so we can`import nessie` in other Python files.






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

    
