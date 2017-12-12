import json
import requests

class BillRequest():

    # perhaps need better way of injecting key?
    def __init__(self, key):
        self.base_url = "http://api.reimaginebanking.com"
        self.key = key
        pass
    
    def get_account_bills(self, account_id):
        url = f'{self.base_url}/accounts/{account_id}/bills/?key={self.key}'
        raise NotImplementedError
        pass


    # Get the bill using the bill_id
    # will return
    # TODO: better way of error handling
    # TODO: better way of appending id
    def get_bill(self, bill_id):
        url = f'{self.base_url}/bills/{bill_id}?key={self.key}' 
        # "/customers/56c66be5a73e492741507273/bills?key="
        response = requests.get(url)
        # if (response.status_code != 200):
        #    error_handle(response)
        result = response.json()
        # need to refactor better
        try:
            result['bill_id']=result['_id']
            del result['_id']
        except KeyError:
            pass
        return result

    def get_customer_bills(self, customer_id):
        url = f'{self.base_url}/customers/{customer_id}/bills?key={self.key}'
        response = requests.get(url)
        #error_handle(response)
        return response.json()

    def get_account_bills(self, account_id):
        url = f'{self.base_url}/accounts/{customer_id}/bills?key={self.key}'
        response = requests.get(url)
        return response.json()

    #
    def create_bill(self, account_id, bill):
        url = f'{self.base_url}/accounts/{account_id}/bills?key={self.key}'
        response = requests.post(url,json=bill) # change json to Bill class??
        return

    def update_bill(self, bill_id):
        url = f'{self.base_url}/bills/{bill_id}/bills?key={self.key}'
        response = requests.put(url)
        return response.json()

    def delete_bill(self, bill_id):
        url = f'{self.base_url}/bills/{bill_id}/bills?key={self.key}'
        response = requests.delete(url)
        return response.json()


def error_handle(error_response):
    raise Exception(error_response.json())

b = Bill('24bb950537c1164a2fbb1bf2a37c3267')
bi = b.get_bill("5a261c3883a71c405074fcbd")
print(bi)
# r = b.get_customer_bills("5a2614e483a71c405074fcba")
# print(r)