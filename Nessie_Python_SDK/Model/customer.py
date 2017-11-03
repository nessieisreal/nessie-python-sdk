from Model.address import Address

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


