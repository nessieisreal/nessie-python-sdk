import requests

from nessie.utils.constants import baseUrl

class DataRequest():
    def __init__(self,api_key):
        self.key = api_key

    # Can Delete:
    # Accounts, Bills, Customers, Deposits
    # Loans, Purchases, Transfers, Withdrawals

    def delete_data(self, dataType:str):
        url=f'{baseUrl}/data?type={dataType}&?key={self.key}'
        response = requests.delete(url)
        # if (response.status_code != 200):
        #    error_handle(response)
        result = response.json()
        return result
    