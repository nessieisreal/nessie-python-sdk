class Address:
	def __init__(self, streetNumber: str, streetName: str, city: str, state: str, zipcode: str):
		self.streetNumber = streetNumber
		self.streetName = streetName
		self.city = city
		self.state = state
		self.zipcode = zipcode

	def createDict(self):
		addressDict = {}
		addressDict["street_number"] = self.streetNumber
		addressDict["street_name"] = self.streetName
		addressDict["city"] = self.city
		addressDict["state"] = self.state
		addressDict["zip"] = self.zipcode
		return addressDict