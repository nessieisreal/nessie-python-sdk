# base class transaction
# should not be directly used
import requests
from nessie import utils

"""
    Where transaction is a:
        bill
        deposit
        loan
        purchase
        transfer
        withdrawal

    accounts/<account_id>/<transaction>s
        GET     fetch all transaction
        POST    create new transaction under <account_id>

    transaction/<id>
        GET     fetch selected transaction
        PUT     update selected transaction
        DELETE  delete selected transaction
"""

class transactionRequest():
    def __init__(self, api_key, transaction_name:str, transaction_class):
        self.key = api_key
        self.base_url = utils.constants.baseUrl
        self.transaction = transaction_name
        self.transaction_class = transaction_class

    # creates <transaction> under the provided account
    def _create_transaction(self, account_id):
        url = f'{self.base_url}/{account_id}/{self.transaction}?key={self.key}'
        response = requests.post(url)
        result = response.json()
        return result

    # return list of <Transaction> python objects from account
    def _get_account_transactions(self, account_id):
        url = f'{self.base_url}/accounts/{account_id}/{self.transaction}?key={self.key}'
        response = requests.get(url)
        result = response.json()
        
        return result
        # need to do work here to convert json into objects

    def _get_transaction(self, transaction_id):
        url = f'{self.base_url}/{self.transaction}/{transaction_id}?key={self.key}' 
        response = requests.get(url)
        result = response.json()
        return result

    def _update_transaction(self, transaction_id):
        url = f'{self.base_url}/{self.transaction}/{transaction_id}?key={self.key}'
        response = requests.put(url)
        result = response.json()
        return result

    def _delete_transaction(self, transaction_id):
        url = f'{self.base_url}/{self.transaction}/{transaction_id}?key={self.key}'
        response = requests.delete(url)
        result = response.json()
        return result


    
    