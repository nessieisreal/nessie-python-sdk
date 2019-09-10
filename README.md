# Nessie Python SDK

[![Build Status](https://travis-ci.org/nessieisreal/nessie-python-sdk.svg?branch=master)](https://travis-ci.org/nessieisreal/nessie-python-sdk)

Provides Wrapper Functions for Nessie API

## Outline

* [Development Setup](#Development-Setup)
* [Installation](#installation)
* [Usage and Examples](#usage-and-examples)

## Development Setup

Install python 3.6.2 or greater

Setup virtual python environment:

```bash
$ python3 -m pip install pipenv # install pipenv package
$ python3 -m pipenv install     # install dependencies into current pipenv
```

If you are on Windows and you receive errors from running `python3`, you can simply use ```$ python```, without the trailing 3. The reason we had it
before is because some OS's, including macOS and Linux flavors, have two python versions. ```python``` refers to Python 2. 


Since the stable version of this SDK is not pushed to the Python Package Index (PyPI), you will need to install it from this repository. Don't worry! You'll just need a few more `pip` commands and you'll be fine. Follow the steps below.

### Setting environment variables

Go to the [Getting Started Page](http://api.reimaginebanking.com/#getting-started), login with your GitHub account, and you should see your API Key
 under `Here is your API key`. Copy this key because you will need it later.


#### On Windows

To set an environment variable on Windows, open Control Panel and search for `Environment Variables`. Click `Edit environment variables for your account`.
 You can also open up the Start menu and start typing it too. The correct menu should pop up. 

Under `User Variables`, click `New`. For the Variable Name, enter `NESSIE_API_KEY`, and in Variable Value, paste in the actual API key. 

#### On Mac and Linux

You can run this command in the terminal:

```bash
$ export NESSIE_API_KEY=[YOUR_API_KEY_HERE]
```

You can also add your key and it's value into your `~/.bashrc` file. If it don't exist, you can make it. 
There might already be text in there, if the file exists. Find an empty line in the file, and put in your environment variable:

```export NESSIE_API_KEY=[YOUR_API_KEY_HERE]```.

#### On both OS's

If you are using pipenv, you can also create a file called `.env` that will contain all of your application's environment variables. This is a file 
that will store your project's environment variables for you. Simply type:

```NESSIE_API_KEY=[YOUR_API_KEY_HERE]```.

*Warning*: Do NOT commit this file. You should never commit your `.env` file. To avoid accidentally committing it, add it to your `.gitignore`. 
Find out more about the .gitignore file [here](https://help.github.com/en/articles/ignoring-files).


## Installation

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

## Usage and Examples
First, go into your pipenv shell for the pipenv that you just made:
```bash 
$ python3 -m pipenv shell       # enter the pipenv shell for your project  
```

After going through _all_ of those steps, we can use this SDK to write our own application! (finally.) 

You can start by creating a Python file outside of the `nessie` repository that you cloned. We can call it `nessie_hello_world.py`.
While you can write all of your code inside the current local repo, your 
code could get confused with Nessie's. And we don't want that to happen ~~because Nessie will eat your code~~.

### Adding customers, accounts, and deposits

```python
# file ~/Documents/hackathon/nessie_hello_world.py
from nessie.client import Client
from nessie.models.address import Address

def main():
    curr_client = Client()
    customer_factory = curr_client.customer
    new_customer_id = customer_factory.create_customer(
        "Nessy",
        "Notmonster", 
        Address("1600", "Green Street", "Henrico", "VA", "23233")
    ).customer_id

    account_factory = curr_client.account
    new_account_id = account_factory.create_customer_account(
        new_customer_id, 
        "Savings", 
        "Winter is Coming Account", 
        0, 
        100)._id

    deposit_factory = curr_client.deposit
    new_deposit = deposit_factory.create_deposit(new_account_id, "balance", 88).to_dict()['id']

if __name__ == '__main__':
    main()

```         

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

    
