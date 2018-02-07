import requests

from .models.deposit import Deposit
from .utils.exceptions import NessieApiError

class DepositRequest():

    # perhaps need better way of injecting key?
    def __init__(self, key):
        self.base_url = "http://api.reimaginebanking.com"
        self.key = key

    # Get the deposit using the deposit_id
    # TODA: better way of error handling
    # TODA: better way of appending id
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

    def get_account_deposits(self, account_id):
        url = f'{self.base_url}/accounts/{account_id}/deposits?key={self.key}'
        response = requests.get(url)
        return response.json()


    def _create_deposit_json(self, account_id, deposit):
        url = f'{self.base_url}/accounts/{account_id}/deposits?key={self.key}'
        response = requests.post(url,json=deposit) # change json to Deposit class??
        return Deposit(response.json()['objectCreated'])

    #Need optional fields
    def create_deposit(self, account_id:str , medium:str, amount:float, transaction_date:str=None,
        status:str=None, description:str=None):
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
        deposit = self._create_deposit_json(account_id, request)
        return deposit


    def _update_deposit_json(self, deposit_id, depositUpdate):
        url = f'{self.base_url}/deposits/{deposit_id}?key={self.key}'
        response = requests.put(url, json=depositUpdate)
        print(response)
        if (response.status_code != 202):
            raise NessieApiError(response)
        return response.json()

    def update_deposit(self, deposit_id:str, medium:str, amount:float,
        description:str=None):
        request = {
            "medium":medium,
            "amount":amount
        }
        if description is not None:
            request["description"] = description
        depositUpdate = self._update_deposit_json(deposit_id, request)
        return depositUpdate

    def delete_deposit(self, deposit_id):
        url = f'{self.base_url}/deposits/{deposit_id}?key={self.key}'
        response = requests.delete(url)
        if (response.status_code != 204):
            raise NessieApiError(response)
