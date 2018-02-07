import requests

from .models.deposit import Deposit
from .utils.exceptions import NessieApiError

class DepositRequest():

    # perhaps need better way of injecting key?
    def __init__(self, key):
        self.base_url = "http://api.reimaginebanking.com"
        self.key = key

    # Returns the deposit with the specific id
    def get_deposit(self, deposit_id):
        url = f'{self.base_url}/deposits/{deposit_id}?key={self.key}'
        response = requests.get(url)
        # if (response.status_code != 200):
        #    error_handle(response)
        result = response.json()
        try:
            result['deposit_id']=result['_id']
            del result['_id']
        except KeyError:
            pass
        return result

    # Returns the deposits that the account is involved in.
    def get_account_deposits(self, account_id):
        url = f'{self.base_url}/accounts/{account_id}/deposits?key={self.key}'
        response = requests.get(url)
        return response.json()

    # Creates a deposit where the account with the ID specified receives the amount.
    def create_deposit(self, account_id:str , medium:str, amount:float, transaction_date:str=None, status:str=None, description:str=None):
        url = f'{self.base_url}/accounts/{account_id}/deposits?key={self.key}'
        request = {
            "medium":medium,
            "amount":amount
        }
        if transaction_date is not None:
            request["transaction_date"] = transaction_date
        if status is not None:
            request["status"] = status
        if description is not None:
            request["description"] = description

        response = requests.post(url,json=request)
        if (response.status_code != 201):
            raise NessieApiError(response)
        return Deposit(response.json()['objectCreated'])

    # Updates the specific deposit
    def update_deposit(self, deposit_id:str, medium:str, amount:float, description:str=None):
        url = f'{self.base_url}/deposits/{deposit_id}?key={self.key}'
        request = {
            "medium":medium,
            "amount":amount
        }
        if description is not None:
            request["description"] = description

        response = requests.put(url, json=request)
        if (response.status_code != 202):
            raise NessieApiError(response)
        return response.json()

    # Deletes the specific deposit
    def delete_deposit(self, deposit_id):
        url = f'{self.base_url}/deposits/{deposit_id}?key={self.key}'
        response = requests.delete(url)
        if (response.status_code != 204):
            raise NessieApiError(response)
