import requests

from nessie.models.bill import Bill
from nessie.utils.exceptions import NessieApiError

class BillRequest():

    # perhaps need better way of injecting key?
    def __init__(self, key):
        self.base_url = "http://api.reimaginebanking.com"
        self.key = key

    # Get the bill using the bill_id
    # will return
    # TODA: better way of error handling
    # TODA: better way of appending id
    def get_bill(self, bill_id):
        url = f'{self.base_url}/bills/{bill_id}?key={self.key}' 
        # "/customers/56c66be5a73e492741507273/bills?key="
        response = requests.get(url)
        if (response.status_code != 200):
            raise NessieApiError(response)
        result = response.json()
        return Bill(result)

    def get_customer_bills(self, customer_id):
        url = f'{self.base_url}/customers/{customer_id}/bills?key={self.key}'
        response = requests.get(url)
        if (response.status_code != 200):
            raise NessieApiError(response)
        # returns an array of bills in json format
        result = response.json()
        # for each bill in json format convert it to a Bill object
        # using map operator and convert iterator to list
        return list(map(lambda json_bill:Bill(json_bill), result))

    def get_account_bills(self, account_id):
        url = f'{self.base_url}/accounts/{account_id}/bills?key={self.key}'
        response = requests.get(url)
        if (response.status_code != 200):
            raise NessieApiError(response)
        result = response.json()
        return list(map(lambda json_bill:Bill(json_bill), result))
    
    # allows users to create bills by passing in json
    def _create_bill_json(self, account_id, bill_json):
        url = f'{self.base_url}/accounts/{account_id}/bills?key={self.key}'
        response = requests.post(url,json=bill_json)
        if (response.status_code != 201):
            raise NessieApiError(response)
        return Bill(response.json()['objectCreated'])

    # create_bill creates a bill underneath an account_id
    def create_bill(self, account_id:str , status:str, payee:str, 
        nickname:str, payment_date:str, recurring_date:int, payment_amount:int):
        bill = self._create_bill_json(account_id,{
            "status":status,
            "payee":payee,
            "nickname":nickname,
            "payment_date":payment_date,
            "recurring_date":recurring_date,
            "payment_amount":payment_amount
        })
        return bill


    def update_bill(self, bill_id):
        url = f'{self.base_url}/bills/{bill_id}/bills?key={self.key}'
        response = requests.put(url)
        if (response.status_code != 200):
            raise NessieApiError(response)
        return response.json()

    def delete_bill(self, bill_id):
        url = f'{self.base_url}/bills/{bill_id}/bills?key={self.key}'
        response = requests.delete(url)
        if (response.status_code != 200):
            raise NessieApiError(response)
        return response.json()