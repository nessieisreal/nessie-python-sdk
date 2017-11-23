<<<<<<< HEAD
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

=======
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

>>>>>>> 09057a7ccbc092ebcc09e24d342ed07c2ac6c767
    # Creates a customer based on parameters
    # Returns a Customer object with CustomerId
    # TODO: Add error handling
    def createCustomer(self, firstName: str, lastName: str, address):
        header = {"Content-Type":"application/json"}
<<<<<<< HEAD
        payload = {"key":self.key}
=======
        payload = {"key":self.getKey()}
>>>>>>> 09057a7ccbc092ebcc09e24d342ed07c2ac6c767
        body = {
        "first_name":firstName,
        "last_name":lastName,
        "address":address.toDict()
        }
<<<<<<< HEAD
        r = requests.post(utils.constants.customersUrl, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        createdCustomer = Customer()
        createdCustomer.firstName = firstName
        createdCustomer.lastName = lastName
        createdCustomer.address = address
        createdCustomer.customerId = data.get("objectCreated").get("_id")
=======
        r = requests.post(urlConstants.customersUrl, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        print(data)
        createdCustomer = Customer()
        createdCustomer.setFirstName(firstName)
        createdCustomer.setLastName(lastName)
        createdCustomer.setAddress(address.streetNumber, address.streetName, address.city, address.state, address.zipcode)
        createdCustomer.setCustomerId(data.get("objectCreated").get("_id"))
>>>>>>> 09057a7ccbc092ebcc09e24d342ed07c2ac6c767
        return createdCustomer

    # Updates a customer's address based on CustomerId
    # TODO: Add error handling
    def updateCustomer(self, customerId, newAddress):
        header = {"Content-Type":"application/json"}
<<<<<<< HEAD
        payload = {"key":self.key}
        body = {"address":newAddress.toDict()}
        customerUrlwithId = utils.constants.customersIdUrl % customerId
=======
        payload = {"key":self.getKey()}
        body = {"address":newAddress.toDict()}
        customerUrlwithId = urlConstants.customersIdUrl % customerId
>>>>>>> 09057a7ccbc092ebcc09e24d342ed07c2ac6c767
        r = requests.put(customerUrlwithId, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        print(data)
        if data.get("code") == 202:
            return True
        else:
            # Prints the error response if not success
            print(data)
            return False
<<<<<<< HEAD
=======

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


>>>>>>> 09057a7ccbc092ebcc09e24d342ed07c2ac6c767
