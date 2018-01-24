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
        response = requests.delete(url)
        # status_code 200 denotes success
        # status_code 404 denotes success, but no data to delete
        if((response.status_code != 200) and (response.status_code!= 404)):
            raise NessieApiError(response)
        result = response.json()
        return result


    