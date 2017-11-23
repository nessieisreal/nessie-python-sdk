import requests, utils.constants, json
from models.customer import Customer


class CustomerRequests:

    def __init__(self, api_key):
        self.key = api_key

    # Methods Dealing With Customers

    # Get customer for an Account
    # Returns a Customer object who owns the AccountId
    # TODO: Add error handling
    def getCustomerByAccountId(self, accountId):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.key}
        customerUrlwithId = utils.constants.accountsCustomerIdUrl % accountId
        r = requests.get(customerUrlwithId, headers=header, params=payload)
        cust = r.json()
        print(cust)
        return Customer(cust)

    # Get all customers
    # Returns a list of Customer objects
    # TODO: Add error handling
    def getAllCustomers(self):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.key}
        r = requests.get(utils.constants.customersUrl, headers=header, params=payload)
        data = r.json()
        customerList = []
        for cust in data:
            customerList.append(Customer(cust))
        return customerList

    # Get customer by Customer Id
    # Returns a Customer object with the provided Customer Id
    # TODO: Add error handling
    def getCustomerById(self, customerId):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.key}
        customerUrlwithId = utils.constants.customersIdUrl % customerId
        r = requests.get(customerUrlwithId, headers=header, params=payload)
        cust = r.json()
        print(cust)
        return Customer(cust)

    # Creates a customer based on parameters
    # Returns a Customer object with CustomerId
    # TODO: Add error handling
    def createCustomer(self, firstName: str, lastName: str, address):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.key}
        body = {
        "first_name":firstName,
        "last_name":lastName,
        "address":address.toDict()
        }
        r = requests.post(utils.constants.customersUrl, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        createdCustomer = Customer()
        createdCustomer.firstName = firstName
        createdCustomer.lastName = lastName
        createdCustomer.address = address
        createdCustomer.customerId = data.get("objectCreated").get("_id")
        return createdCustomer

    # Updates a customer's address based on CustomerId
    # TODO: Add error handling
    def updateCustomer(self, customerId, newAddress):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.key}
        body = {"address":newAddress.toDict()}
        customerUrlwithId = utils.constants.customersIdUrl % customerId
        r = requests.put(customerUrlwithId, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        print(data)
        if data.get("code") == 202:
            return True
        else:
            # Prints the error response if not success
            print(data)
            return False
