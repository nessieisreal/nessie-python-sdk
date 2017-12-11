import requests
import utils.constants
import json
from models.customer import Customer
from utils.exceptions import ATMValidationError, NessieApiError


class CustomerRequests:

    def __init__(self, api_key):
        self.key = api_key

    # Methods Dealing With Customers

    # Get customer for an Account
    # Returns a Customer object who owns the AccountId
    def get_customers_by_account_id(self, account_id):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        url = utils.constants.accountsCustomerIdUrl % account_id
        r = requests.get(url, headers=header, params=payload)
        return Customer(r.json())

    # Get all customers
    # Returns a list of Customer objects
    def get_all_customers(self):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        r = requests.get(utils.constants.customersUrl, headers=header, params=payload)
        if r.status_code != 200:
            raise NessieApiError(r)
        data = r.json()
        customer_list = []
        for c in data:
            customer_list.append(Customer(c))
        return customer_list

    # Get customer by Customer Id
    # Returns a Customer object with the provided Customer Id
    def get_customer_by_id(self, customer_id):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        url = utils.constants.customersIdUrl % customer_id
        r = requests.get(url, headers=header, params=payload)
        if r.status_code != 200:
            raise NessieApiError(r)
        return Customer(r.json())

    # Creates a customer based on parameters
    # Returns a Customer object with CustomerId
    def create_customer(self, first_name: str, last_name: str, address):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        body = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address.to_dict()
        }
        r = requests.post(utils.constants.customersUrl, headers=header, params=payload, data=json.dumps(body))
        if r.status_code != 200:
            raise NessieApiError(r)
        data = r.json()
        created_customer = Customer()
        created_customer.first_name = first_name
        created_customer.last_name = last_name
        created_customer.address = address
        created_customer.customer_id = data.get("objectCreated").get("_id")
        return created_customer

    # Updates a customer's address based on CustomerId
    def update_customer(self, customer_id, new_address):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        body = {"address": new_address.to_dict()}
        url = utils.constants.customersIdUrl % customer_id
        r = requests.put(url, headers=header, params=payload, data=json.dumps(body))
        if r.status_code != 202:
            raise NessieApiError(r)
        else:
            return True
