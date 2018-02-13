import requests

from .transactionRequests import TransactionRequest
from .models.transfer import Transfer
from .utils.constants import baseUrl

class TransferRequests():
    def __init__(self, api_key):
        self.key = key
    
    # a GET request for transfer with 
    # corresponding transfer_id
    def get_transfer(self, transfer_id):
        url = f'{baseUrl}/transfers/{transfer_id}?key={self.key}'
        response = requests.get(url)
        if (response.status_code != 200):
            raise NessieApiError(response)
    
    # GET request to fetch all transfer transactions
    # from the specified account
    def get_transfers_of_account(self, account_id):
        url = f'{baseUrl}/accounts/{account_id}/transfers?key={self.key}'
        
    def create_transfer(self,medium,payee_id,transaction_date, status,description):
        url = f'{baseUrl}/accounts/{account_id}/transfers?key={self.key}'
        
        body = {
            'medium': medium,
            'payee_id': payee_id,
            'transaction_date': transaction_date,
            'status': status,
            'description':description
        }
        response = requests.post(url, json=body)