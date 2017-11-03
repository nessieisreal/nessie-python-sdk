import requests, json, urlConstants
from Model.address import Address
from Model.customer import Customer

class CustomerRequests:
    def __init__(self, apiKey):
        self.key = apiKey
    def getKey(self):
        if self.key == "":
            print("No key is present. An api key is required to send requests")
        return self.key
    def setKey(apiKey):
        self.key = apiKey

    # Methods Dealing With Customers

    # Creates a customer based on parameters
    # Returns a Customer object with CustomerId
    # TODO: Add error handling
    def createCustomer(self, firstName: str, lastName: str, address):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.getKey()}
        body = {
        "first_name":firstName,
        "last_name":lastName,
        "address":address.toDict()
        }
        r = requests.post(urlConstants.customersUrl, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        print(data)
        createdCustomer = Customer()
        createdCustomer.setFirstName(firstName)
        createdCustomer.setLastName(lastName)
        createdCustomer.setAddress(address.streetNumber, address.streetName, address.city, address.state, address.zipcode)
        createdCustomer.setCustomerId(data.get("objectCreated").get("_id"))
        return createdCustomer

    # Updates a customer's address based on CustomerId
    # TODO: Add error handling
    def updateCustomer(self, customerId, newAddress):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.getKey()}
        body = {"address":newAddress.toDict()}
        customerUrlwithId = urlConstants.customersIdUrl % customerId
        r = requests.put(customerUrlwithId, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        print(data)
        if data.get("code") == 202:
            return True
        else:
            # Prints the error response if not success
            print(data)
            return False

    # Creates a Customer Object from python dictonary representation
    @staticmethod
    def __customerDictToObj(cust):
        convertedCustomer = Customer()
        convertedCustomer.setFirstName(cust.get("first_name"))
        convertedCustomer.setLastName(cust.get("last_name"))
        convertedCustomer.setAddress(cust.get("street_number"), cust.get("street_name"), cust.get("city"), cust.get("state"), cust.get("zip"))
        convertedCustomer.setCustomerId(cust.get("_id"))
        return convertedCustomer

    # Get all customers
    # Returns a list of Customer objects
    # TODO: Add error handling
    def getAllCustomers(self):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.getKey()}
        r = requests.get(urlConstants.customersUrl, headers=header, params=payload)
        data = r.json()
        customerList = []
        for cust in data:
            createdCustomer = CustomerRequests.__customerDictToObj(cust)
            customerList.append(createdCustomer)
        return customerList

    # Get customer by Customer Id
    # Returns a Customer object with the provided Customer Id
    # TODO: Add error handling
    def getCustomerById(self, customerId):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.getKey()}
        customerUrlwithId = urlConstants.customersIdUrl % customerId
        r = requests.get(customerUrlwithId, headers=header, params=payload)
        cust = r.json()
        print(cust)
        return CustomerRequests.__customerDictToObj(cust)


