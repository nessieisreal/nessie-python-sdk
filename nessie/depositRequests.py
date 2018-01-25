import requests

from nessie.models.deposit import Deposit

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
    def create_deposit(self, account_id:str , medium:str, transaction_date:str,
        status:str, amount:float, description:str):
        deposit = self._create_deposit_json(account_id,{
            "medium":medium,
            "transaction_date":transaction_date,
            "status":status,
            "amount":amount,
            "description":description
        })
        return deposit


    def _update_deposit_json(self, deposit_id, depositUpdate):
        url = f'{self.base_url}/deposits/{deposit_id}/deposits?key={self.key}'
        response = requests.put(url, json=depositUpdate)
        print(response)
        return response.json()

    def update_deposit(self, deposit_id:str, medium:str, amount:float,
        description:str):
        depositUpdate = self._update_deposit_json(deposit_id,{
            "medium":medium,
            "amount":amount,
            "description":description
        })
        return depositUpdate

    def delete_deposit(self, deposit_id):
        url = f'{self.base_url}/deposits/{deposit_id}/deposits?key={self.key}'
        response = requests.delete(url)
        return response.json()


def error_handle(error_response):
    raise Exception(error_response.json())
