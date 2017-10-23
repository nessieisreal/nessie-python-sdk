import requests, json

from urlConstants import *
from address import *

class Customer:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.address = None
        self.customerId = ""

    def setFirstName(self, firstName: str):
        self.firstName = firstName
    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName: str):
        self.lastName = lastName
    def getLastName(self):
        return self.lastName

    def setAddress(self, streetNumber: str, streetName: str, city: str, state: str, zipcode: str):
        self.address = Address(streetNumber, streetName, city, state, zipcode)
    def getAddress(self):
        return self.address

    def setCustomerId(self, customerId: str):
        self.customerId = customerId
    def getCustomerId(self):
        return self.customerId


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
    def createCustomer(self, firstName: str, lastName: str, address):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.getKey()}
        body = {
        "first_name":firstName,
        "last_name":lastName,
        "address":address.createDict()
        }
        r = requests.post(customersUrl, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        print(data)
        createdCustomer = Customer()
        createdCustomer.setFirstName(firstName)
        createdCustomer.setLastName(lastName)
        createdCustomer.setAddress(address.streetNumber, address.streetName, address.city, address.state, address.zipcode)
        createdCustomer.setCustomerId(data.get("objectCreated").get("_id"))
        return createdCustomer

    # Updates a customer's address based on CustomerId
    def updateCustomer(self, customerId, newAddress):
        header = {"Content-Type":"application/json"}
        payload = {"key":self.getKey()}
        body = {
        "address":newAddress.createDict()
        }
        customerUrlwithId = customersIdUrl % customerId
        r = requests.put(customerUrlwithId, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        if data.get("code") == 202:
            return True
        else:
            # Prints the error response if not success
            print(data)
            return False

#     # Creates a customer based on Customer Object
#     # Returns Customer object with CustomerId
#     def createCustomerWithObject(customer: Customer):

# def main():
#     client = NessieClient("6d710f1c84683f0aa00f8888e12a9e59")
#     myLat = 38.9283
#     myLng = -77.1753
#     myRad = 10

#     atmData = client.getAtms(lat=myLat, lng=myLng, rad=myRad)
#     print(atmData)

# if __name__ == '__main__':
#     main()