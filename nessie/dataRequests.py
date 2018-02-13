import requests

from .utils.constants import baseUrl
from .utils.exceptions import NessieApiError

class DataRequests():
    def __init__(self,api_key):
        self.key = api_key

    # Can Delete:
    # Accounts, Bills, Customers, Deposits
    # Loans, Purchases, Transfers, Withdrawals

    def delete_data(self, dataType:str):
        url=f'{baseUrl}/data?type={dataType}&key={self.key}'
        # 'Connection':'close',
        headers = { 'Content-type': 'application/json'}
        response = requests.delete(url, headers=headers)
        # status_code 200 denotes success
        # status_code 404 denotes success, but no data to delete
        if(
            (response.status_code != 200) and 
            (response.status_code != 204) and 
            (response.status_code != 404)):
            raise NessieApiError(response)
            
        # sometimes the response encoding is nothing
        # rather than utf-8 so the response.json() 
        # will crash
        if (response.encoding is None):
            return {}
            
        result = response.json()
        return result


    